"""Reads items.json -> writes index.html (self-contained, works offline, themed light/dark)."""
import json
L7=["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
G7=["0100111","0110011","0011011","0100001","0011101","0111001","0000101","0010001","0001001","0010111"]
R7=["1110010","1100110","1101100","1000010","1011100","1001110","1010000","1000100","1001000","1110100"]
PAR=["LLLLLL","LLGLGG","LLGGLG","LLGGGL","LGLLGG","LGGLLG","LGGGLL","LGLGLG","LGLGGL","LGGLGL"]
def valid(d):
    return d.isdigit() and len(d) in (8,13) and (10-sum(int(c)*(3 if (len(d)-1-i)%2 else 1) for i,c in enumerate(d[:-1]))%10)%10==int(d[-1])
def bits(c):
    if len(c)==13:
        p=PAR[int(c[0])]
        return "101"+"".join((L7 if p[i]=="L" else G7)[int(x)] for i,x in enumerate(c[1:7]))+"01010"+"".join(R7[int(x)] for x in c[7:])+"101"
    return "101"+"".join(L7[int(x)] for x in c[:4])+"01010"+"".join(R7[int(x)] for x in c[4:])+"101"
def svg(c):
    """Self-contained barcode image (white background baked in) as a data URI.
    Keeping background + bars inside one image stops device 'force dark' modes
    from inverting only half of it."""
    import base64
    b=bits(c);q=9;w=len(b)+2*q
    bars="".join(f'<rect x="{q+i}" width="1" height="60"/>' for i,x in enumerate(b) if x=="1")
    s=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 60" width="{w*4}" height="240" preserveAspectRatio="none" shape-rendering="crispEdges">'
       f'<rect width="{w}" height="60" fill="#fff"/><g fill="#000">{bars}</g></svg>')
    return "data:image/svg+xml;base64,"+base64.b64encode(s.encode()).decode()
items=json.load(open("items.json",encoding="utf-8"))
for it in items:
    assert valid(it["ean"]),("bad barcode",it)
    it["uri"]=svg(it["ean"])
data=json.dumps(items,ensure_ascii=False).replace("</","<\\/")
page=open("template.html",encoding="utf-8").read().replace("/*DATA*/[]",data)
open("index.html","w",encoding="utf-8").write(page)
print(len(items),"items built")
