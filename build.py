import html
# (receipt name, product matched, EAN, confidence) ; H = strong match, M = likely, L = check size/flavour in app
ITEMS=[
("B/DRAGON CHOW MEIN","Blue Dragon Chow Mein Stir Fry Sauce 120g","5010338200060","H"),
("B/DRAGON EGG NOODLES","Blue Dragon Fine Egg Noodles 250g","5010338103774","M"),
("BOURSIN CHEESE","Boursin Garlic & Herbs 150g","3175460000017","M"),
("DOVE ROLL ON","Dove Roll On Deodorant 50ml","80466444","L"),
("GARNIER OLIA","Garnier Olia hair colour (shade unknown)","3600541233270","L"),
("M BRIT S/SKIM MILK","Morrisons British Semi Skimmed Milk 4 pint","5010251268192","L"),
("M DOUBLE CREAM","Morrisons Double Cream 300ml","5010251341352","H"),
("M GARLIC CHICK/KIEVS","Morrisons Garlic Chicken Kievs","5010251603658","M"),
("M SPIRALI PASTA","Morrisons Spirali 500g","5010525013091","H"),
("M SWEETCORN","Morrisons Sweetcorn in Water","5010251834472","M"),
("M TOASTIE WHITE LOAF","Morrisons Toastie White 800g","5010251737117","H"),
("POT NOODLE CHOW MEIN","Pot Noodle Chinese Chow Mein 90g","5000118203534","H"),
("LENOR CONDITIONER","Lenor Conditioner","8700216673181","L"),
("CADBURY TWIRL","Cadbury Twirl","5000201499776","M"),
("KENDAMIL FORMULA","Kendamil First Infant Milk 800g (your list has Comfort - scan that one if it's Comfort)","5056000505910","M"),
("M HAM+CHEESE S/W","Morrisons Ham & Cheese Sandwich","5010251797777","M"),
("MALTESERS","Maltesers 135g","5000159555692","L"),
("NISSIN SOBA YAKITORI","Nissin Soba Cup Yakitori 89g","5997523311230","M"),
("REDBULL ENERGY DRINK","Red Bull Energy Drink 250ml","90162602","H"),
("WALKERS MAX PAPRIKA","Walkers Max Punchy Paprika","5000328019390","L"),
("ELLA'S KIT MELT STICKS","Ella's Kitchen Melty Sticks","5060107339811","M"),
("GINSTERS PASTY","Ginsters Cornish Pasty 180g","5010718204817","M"),
("HEINZ BISCOTTI","Heinz Banana Biscotti","5000157070609","L"),
("M BREAKFAST WRAP","Morrisons All Day Breakfast Wrap","5010525356723","M"),
("M PASTA SAUCE","Morrisons Tomato & Garlic Pasta Sauce","5010251460305","L"),
("M TOILET TISSUE","Morrisons Soft Toilet Tissue","5010251781615","L"),
("M TORTELLONI","Morrisons Spinach & Ricotta Tortelloni 300g","5010251595243","L"),
("PASTA N SCE CHS+BROC","Batchelors Pasta 'n' Sauce Cheese & Broccoli","5000354404009","H"),
("HAZLEMERE VINEGAR","Hazlemere Apple Cider Vinegar","5060608080298","L"),
("KELLOGGS POP TARTS","Kellogg's Pop-Tarts","5059320000011","M"),
("M BOLOGNESE SAUCE","Morrisons Bolognese Pasta Sauce","5010251460299","L"),
("M EX MATURE GRATED","Morrisons Extra Mature Grated Cheddar","5010525276038","H"),
("M FROMAGE FRAIS","Morrisons Fromage Frais 4x80g","5010251948582","L"),
("M FUSILLI","Morrisons Fusilli 3kg","5010251461029","L"),
("MULLER CORNER OREO","Müller Corner x Oreo","4025500307721","M"),
("MULLER CORNER YOGURT","Müller Corner yogurt (flavour unknown)","4025500277642","L"),
("NESTLE SHREDDIES","Nestlé Shreddies 630g","7613287152183","L"),
("PETITS FILOUS YOGURT","Petits Filous 4x100g","3329775188230","L"),
("WARBURTON LOAF","Warburtons Medium Toastie White 800g","5010044000039","L"),
("LUCOZADE ENERGY ZERO","Lucozade Energy Zero Sugar","5054267011021","L"),
("M BAKED BEANS","Morrisons Baked Beans 410g","5010251569190","L"),
("M INST NOODLES CHKN","Morrisons Chicken Flavour Noodles 85g","5010251618843","H"),
("SUPER NOODLES CURRY","Batchelors Super Noodles Curry 90g","5000354914409","H"),
("CADBURY BUTTONS","Cadbury Dairy Milk Buttons 100g","7622202258480","M"),
("GALPHARM PARACETAMOL","Galpharm Paracetamol","5017353500809","M"),
("HNZ CAUL BROC CHEESE","Heinz Cauliflower Broccoli Cheese","5000157141477","L"),
("JELLY TOTS TANGY","Rowntree's Jelly Tots Tangy 140g","8445291508644","H"),
("JIMMY'S ICED COFFEE","Jimmy's Iced Coffee Original 380ml","5010102004061","M"),
("MONSTER ULTRA DRINK","Monster Energy Ultra 500ml","5060335635174","L"),
("COUNTRY LIFE","Country Life Butter 750g","5000295143630","L"),
("FAIRY WASHING LIQUID","Fairy Washing Up Liquid","4084500900509","L"),
("FYFFES BANANAS 5PK","Fyffes Bananas","5397005919402","L"),
("M CHICKEN POPPERS","Morrisons BBQ Chicken Poppers","5010525396552","L"),
("M CHICKEN SKEWERS","Morrisons BBQ Chicken Skewers 100g","5010251795506","L"),
("M COCKTAIL SAUSAGES","Morrisons Cocktail Sausages","5010251749417","L"),
("M MINI BITESIZE EGGS","Morrisons 4 Mini Savoury Eggs","5010525401928","L"),
("M QUICHE LORRAINE","Morrisons Quiche Lorraine","5010251589341","L"),
("M SLT&VINEGAR TWIRLS","Morrisons Salt & Vinegar Twirls 125g","5010251597322","H"),
("SKIPS PRAWN COCKTAIL","Skips Prawn Cocktail","5000237206539","L"),
]
NONE=[
"B/DRAGON STIRY FRY","M RED ONIONS","M BAG FOR LIFE / M REUSABLE BAG / M THE BEST BAG (carrier bags - just add as 'Other')","MORRISONS GARLIC (unclear what product)","BOLD PODS","LENOR SCENT BOOSTER","BABY BASICS / BABY FASHION NON VAT (clothing)","BODYFORM TOWELS","NUTMEG MATERNITY TOWELS, TOMATO+PASTA, VEG+CHICK/CAS, WIPES, BEDTIME BATH, NAPPIES","M GRATED GARL+HERB","M PINK LADY APPLES (the list already has 'Pink Lady Apples 4 Pack')","MULLER CORNER COLLAB","EL KIT BABY BREKKIE, EL/KITCH FRUIT POUCH, ELLA'S BABY FOOD, ELLA'S KITCHEN (flavours unknown)","KINDER SURPRISE EGGS","REDBULL - done above"]
NONE=[n for n in NONE if "done above" not in n]
L7=["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
G={"L":L7,"G":["0100111","0110011","0011011","0100001","0011101","0111001","0000101","0010001","0001001","0010111"],"R":["1110010","1100110","1101100","1000010","1011100","1001110","1010000","1000100","1001000","1110100"]}
PAR=["LLLLLL","LLGLGG","LLGGLG","LLGGGL","LGLLGG","LGGLLG","LGGGLL","LGLGLG","LGLGGL","LGGLGL"]
def chk(d):
    s=sum(int(c)*(3 if (len(d)-1-i)%2==1 else 1) for i,c in enumerate(d[:-1]))
    return (10-s%10)%10==int(d[-1])
def bits(code):
    if len(code)==13:
        p=PAR[int(code[0])];b="101"
        for i,c in enumerate(code[1:7]): b+=G[p[i]][int(c)]
        b+="01010"
        for c in code[7:]: b+=G["R"][int(c)]
        return b+"101"
    b="101"+"".join(G["L"][int(c)] for c in code[:4])+"01010"+"".join(G["R"][int(c)] for c in code[4:])+"101"
    return b
def svg(code):
    b=bits(code);q=9;w=len(b)+2*q
    bars="".join(f'<rect x="{q+i}" y="0" width="1" height="60"/>' for i,x in enumerate(b) if x=="1")
    return f'<svg viewBox="0 0 {w} 60" preserveAspectRatio="none" role="img" aria-label="barcode {code}" fill="#000">{bars}</svg>'
bad=[i for i in ITEMS if not chk(i[2])]
assert not bad, bad
lab={"H":"Strong match","M":"Likely match","L":"Check in app"}
def card(i):
    r,n,c,k=i
    return f'<div class="card" tabindex="0"><div class="tag {k}">{lab[k]}</div><div class="bc">{svg(c)}</div><div class="num">{c}</div><div class="nm">{html.escape(n)}</div><div class="rc">Receipt: {html.escape(r)}</div></div>'
out=["""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Receipt barcodes</title><style>
body{font-family:system-ui,sans-serif;margin:0;padding:16px;background:#f4f4f4;color:#111}
h1{margin:0 0 4px}p.s{margin:0 0 16px;color:#444;max-width:60ch}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}
.card{background:#fff;border-radius:10px;padding:12px;border:2px solid #ddd;cursor:pointer}
.card:focus,.card.big{position:fixed;inset:0;z-index:9;margin:auto;max-width:92vw;height:fit-content;box-shadow:0 0 0 100vmax rgba(0,0,0,.7);outline:none}
.bc{background:#fff;padding:6px 0}.bc svg{width:100%;height:90px;display:block}.card:focus .bc svg{height:180px}
.num{font:600 15px monospace;text-align:center;letter-spacing:1px}.nm{font-weight:600;margin-top:6px}.rc{color:#666;font-size:12px}
.tag{font-size:11px;font-weight:700;padding:2px 8px;border-radius:99px;display:inline-block;margin-bottom:4px}
.H{background:#cdeccd;color:#14501a}.M{background:#fff0b8;color:#6b5200}.L{background:#ffd9d4;color:#7a1d10}
h2{margin:24px 0 8px}li{margin:4px 0}</style></head><body>
<h1>Receipt items &rarr; barcodes</h1>
<p class="s">Tap a barcode to enlarge it, then scan it with the barcode button in the Morrisons app shopping list (turn screen brightness up). Barcodes came from Open Food Facts, matched from receipt names, which don't show size or flavour, so check the product the app shows before adding. <b>Strong</b> = confident; <b>Likely</b> = right product, size may differ; <b>Check</b> = guess.</p>"""]
for k,t in (("H","Strong matches"),("M","Likely matches"),("L","Check in app")):
    out.append(f'<h2>{t}</h2><div class="grid">'+"".join(card(i) for i in ITEMS if i[3]==k)+'</div>')
out.append('<h2>No barcode found</h2><p class="s">Not in the free database. Add these by typing the name in the app.</p><ul>'+"".join(f"<li>{html.escape(n)}</li>" for n in NONE)+'</ul>')
out.append("""<script>document.querySelectorAll('.card').forEach(c=>c.addEventListener('click',()=>{if(document.activeElement===c)c.blur();else c.focus()}))</script></body></html>""")
open("index.html","w").write("\n".join(out))
print(len(ITEMS),"barcodes; all check digits valid;",len(NONE),"unmatched")
