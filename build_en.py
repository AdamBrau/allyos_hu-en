import os
import shutil
import re

translations = {
    # Navigáció és közös elemek
    "Skip to content": "Skip to content",
    "Letöltés": "Download",
    "A Platformról": "About Platform",
    "Influenszereknek": "For Influencers",
    "Partnereknek": "For Partners",
    "Hírek": "News",
    "Rólunk": "About Us",
    "Kapcsolat": "Contact",
    "GYIK": "FAQ",
    "Adatvédelem": "Privacy Policy",
    "ÁSZF": "Terms & Conditions",
    "Újragondoltuk a vásárlást. Benne vagy?": "We reimagined shopping. Are you in?",
    "Social Shopping is a registered patent owned by Allyos Europe Ltd.": "Social Shopping is a registered patent owned by Allyos Europe Ltd.",
    "A beleegyezés kezelése": "Manage Consent",
    "Funkcionális": "Functional",
    "Always active": "Always active",
    "Statisztika": "Statistics",
    "Marketing": "Marketing",
    "Preferences": "Preferences",
    "Manage options": "Manage options",
    "Manage services": "Manage services",
    "Read more about these purposes": "Read more about these purposes",
    "Elfogadom": "Accept",
    "Elutasítom": "Decline",
    "Beállítások megtekintése": "View preferences",
    "Mentsd el a beállításokat": "Save preferences",
    "Scroll to Top": "Scroll to Top",

    # Főoldal
    "DRÁGA...?": "EXPENSIVE...?",
    "DOBJUK ÖSSZE!": "LET'S POOL IT!",
    "Új közösségi platform a közös vásárlásra.": "A new social platform for group shopping.",
    "Szállj be kedvenc márkáid közös vásárlásába, amihez levásárolható kedvezményt adnak.": "Join group purchases of your favorite brands backed by redeemable discounts.",
    "Töltsd le és regisztrálj profilt te is!": "Download the app and create your profile today!",
    "DRÁGA A LUXUSKATEGÓRIA?": "IS LUXURY TOO EXPENSIVE?",
    "Ahogy eddig vásároltál igen, mert egyedül kellett kicsengetned az árat.": "The old way, yes—because you had to pay the full price alone.",
    "Ahogy eddig vásároltál igen, mert egyedül kell kicsengetned az árat.": "The old way, yes—because you have to pay the full price alone.",
    "De ha az árát együtt dobnánk össze, megérne az új kedvenc autód 3500 forintot, ha ezért a tiéd is lehet?": "But if we pooled the money together, would your dream car be worth $10 to you if it could be yours?",
    "EZ A\nKÖZÖSSÉGI VÁSÁRLÁS™!": "THIS IS\nSOCIAL SHOPPING™!",
    "EZ A\nKÖZÖSSÉGI\nVÁSÁRLÁS™!": "THIS IS\nSOCIAL\nSHOPPING™!",
    "Olcsó alternatívák helyett így vehetsz prémium és luxuskategóriás termékeket.": "Instead of cheap alternatives, get premium and luxury goods this way.",
    "Szállj be számodra kényelmes összeggel, és legyen a tiéd, ha összedobtuk az árát.": "Join with an amount comfortable for you, and take it home once the goal is reached.",
    "ÉLMÉNY A MAXON, PARA A PADLÓN.": "MAXIMUM THRILL, ZERO RISK.",
    "ÉLMÉNY A MAXON,\nPARA A PADLÓN.": "MAXIMUM THRILL,\nZERO RISK.",
    "Közösségi Vásárlásban csak levásárolható kedvezménnyel lehet részt venni.": "In Social Shopping, participation is backed entirely by redeemable discounts.",
    "Ha sikerült összedobni, egy szerencsés a terméket, a többiek vásárlási utalványt kapnak vissza.": "Once funded, one buyer gets the product, and everyone else receives shopping credits back.",
    "KÖVESS BE, KÖSZÖNJ BE!": "FOLLOW & CONNECT!",
    "Kövesd be kedvenc influenszered a platformon és csatlakozz vele egy csapatba.": "Follow your favorite influencers on the platform and join their shopping team.",
    "Dobjátok össze együtt, amit tegnap még csak nézegettél, mert túl drága volt. Köszönj be chaten is.": "Pool together for items you only dreamed of yesterday. Say hi in the chat too.",
    "Ne maradj ki a vásárlás fejlődéséből.": "Don't miss the evolution of e-commerce.",
    "Csatlakozz az online vásárlást felváltó Közösségi Vásárlókhoz.": "Join the Social Shoppers replacing traditional online commerce.",
    "Gyártó és forgalmazó ajánlatai": "Direct manufacturer and distributor offers",
    "350Ft": "$1",
    "Minimum beszálló": "Minimum entry",
    "Levásárolható részvétel": "100% redeemable participation",
    "Vásárlási eredmény": "Shopping success rate",
    "Hamarosan elérhető": "Coming soon",
    "a megújult verzió!": "the redesigned version!",
    "Amikor a Livestream shopping találkozik a Social Commerce-szel az Allyos keretein belül, az mindent megváltoztat, amit eddig ismertünk.": "When Livestream shopping meets Social Commerce inside Allyos, everything we know about commerce changes.",
    "Megjelent a legújabb méregdrága cucc amire vágytál?": "Did the latest premium gear you wanted just drop?",
    "3 lépés választ el tőle.": "You're only 3 steps away.",
    "Töltsd le az appot!": "Download the app!",
    "Regisztrálj profilt!": "Create a profile!",
    "Szállj be!": "Jump in!",
    "Ezért uncsi a social mediánk!": "Why settle for boring social media?",
    "Élményért gyere a SocialStore-ba!": "Join SocialStore for real excitement!",
    "Élményért gyere\na SocialStore-ba!": "Join SocialStore\nfor real excitement!",
    "Legyen az első részvétel INGYEN?": "Want your first participation for FREE?",
    "Igen, mutasd!": "Yes, show me!",
    "A social mediánk uncsi.": "Traditional social media is boring.",
    "Élményért a SocialStore-ba gyere!": "Join SocialStore for real experiences!",
    "Élményért a\nSocialStore-ba gyere!": "Join SocialStore\nfor real experiences!",

    # Platform oldal
    "A vásárlás új szintje": "The Next Level of Shopping",
    "A platform ezzel ideális teret nyit a termék vagy szolgáltatás promótáló és tesztelő influenszereknek is, mivel a követőik széles körének válik elérhetővé mindaz, ami eddig túl drága volt.": "The platform opens up ideal avenues for influencers reviewing and showcasing products, making premium goods accessible to all their followers.",
    "A Közösségi Vásárlás™": "Social Shopping™",
    "Alacsony részvétel": "Low entry barrier",
    "Együtt dobjuk össze": "We pool it together",
    "Ha többet is adnál a termékért, óránként 1 dollárral emelheted a részvételi licitet.": "If you'd contribute more, you can increase your bid by $1 every hour.",
    "Az ár fix": "The price is fixed",
    "Amennyit neked megér": "As much as it's worth to you",
    "Így tudod elkezdeni": "How to get started",
    "Vagy feltöltöd az egyenleged": "Top up your balance",
    "Vagy bónuszt kapsz vásárlással": "Or earn bonus credits via shopping",
    "Üdvözlünk a\nKözösségi Vásárlók körében!": "Welcome to the\nCommunity of Social Shoppers!",

    # Influenszerek oldal
    "Új közösségi platform": "A New Social Platform",
    "Vásárlás követőiddel közösen": "Shop Together With Your Followers",
    "Rekordmagas kereset": "Record High Earnings",
    "7 millió forint havonta 10.000 követővel a platformon az átlag jövedelem, amivel a legjobban fizető közösségi platform státuszába került.": "Earn up to $20,000 monthly with 10,000 followers, making it the highest-paying social commerce platform.",
    "Minden egyes a tartalmadban bemutatott termék eladásával az árának 10%-a kerül jóváírásra a számládon.": "Earn 10% commission on the full product value for every item funded through your content.",
    "Hozzáférés prémium szponzorokhoz": "Access to Premium Sponsors",
    "5 millió forint a starthoz": "Kickstart funding for creators",
    "Nincs AI-influencer konkurencia": "Zero AI-Influencer Competition",
    "Töltsd ki a formot!": "Fill out the form!",
    "Jelentkezz VIP-profilért. Kollégáink felveszik veled a kapcsolatot, és segítenek a teljes folyamatban.": "Apply for a VIP profile. Our team will contact you and guide you through every step.",
    "Elolvastam és elfogadom az adatvédelmi nyilatkozatot!": "I have read and agree to the Privacy Policy!",
    "Elküldöm!": "Submit!",

    # Partnerek oldal
    "Mik a közösségi értékesítés előnyei?": "Benefits of Social Commerce",
    "Megszabadít az árversenytől": "Eliminate Price Competition",
    "Nagyobb profit, dupla darabszám": "Higher Margins, Double Volume",
    "Teljes európai piac díjtalanul": "Access the Entire European Market Free",
    "Ingyenes influenszer kampány": "Free Influencer Campaigns",
    "Kérj díjmentes ajánlatot!": "Request a Free Consultation!",
    "Töltsd ki az adatlapot, hogy asszisztens kollégáink felvehessék veled a kapcsolatot. Segítenek partnerként arculatodra szabott influenszer kiválasztásában és promóció elindításában.": "Complete the form so our specialists can reach out to help connect your brand with tailored influencers and launch campaigns.",

    # Kapcsolat oldal
    "Kérdés esetén állunk rendelkezésedre.": "We are here to assist you.",
    "Ha kérdésed van, szívesen segítünk!": "Have questions? We're happy to help!",
    "Válaszd ki a témakört és töltsd ki az adatokat:": "Select a category and fill in your details:",
    "Általános segítség": "General Support",
    "IT részleg": "IT Support",
    "Termék osztály": "Product Department",
    "Fiók segítség": "Account Help",
    "Egyéb kérdés": "Other Inquiry",
    "Európai Divízió": "European Division",
    "Szoftver Fejlesztés": "Software Development",
    "USA Divízió": "USA Division",
    "Licensz és Jogok": "Licensing & Rights",

    # Rólunk oldal
    "A kereskedelem reformja": "Reforming Commerce",
    "Az iPhone problémával kezdődött minden": "It all started with the iPhone dilemma",
    "Az innovátor megérkezése": "Arrival of the Innovator",
    "Újragondolt e-commerce": "Reimagined E-Commerce",
    "Allyos csapat": "Allyos Team",
    "Nagyobb cél felé": "Toward a Greater Purpose",
    "Az amerikai álom magyar fejlesztéssel élhető": "Scaling the Vision Globally",
    "Közös vásárlás, globális siker": "Group Buying, Global Success",
    "E-commerce kerekasztal": "E-Commerce Roundtable",

    # GYIK oldal
    "Help Center": "Help Center",
    "Az Appról": "About the App",
    "Termékek és kiszállítás": "Products & Shipping",
    "Technikai kérdések": "Technical Questions",
    "Mi az Allyos?": "What is Allyos?",
    "Mi a SocialStore?": "What is SocialStore?",
    "Ingyenes a platform használata?": "Is the platform free to use?",
    "Mi az a „közösségi vásárlás”?": "What is 'Social Shopping'?",
    "Sikeres közösségi vásárlás során csak egyvalaki veheti meg a terméket?": "In a successful group buy, does only one person get the item?",
    "Ha én lettem a kiválasztott, automatikusan enyém a termék?": "If selected, do I automatically own the product?",
    "Mennyi időm van elfogadni a vásárlás jogát?": "How long do I have to accept the purchase option?",
    "Hogyan értesítenek arról, ha én lettem a szerencsés vásárló?": "How will I be notified if I am selected?",
    "Mennyi idő alatt kell közösen összedobni egy termék árát?": "How much time is available to fund a product?",
    "Miért van szükség fix lejárati időre?": "Why is there a fixed expiration time?",
    "Mennyi a minimum részvételi összeg, amivel csatlakozni lehet egy közösségi vásárláshoz?": "What is the minimum amount to join a group buy?",
    "Mekkora a legmagasabb részvételi összeg, amivel egy közösségi vásárló részt vehet?": "What is the maximum amount an individual can contribute?",
    "Hány emberre van szükség egy sikeres közösségi vásárláshoz?": "How many participants are needed for a successful purchase?",
    "Ha növelem a betett összegemet egy terméknél, az esélyeim is nőnek arra, hogy kiválasztásra kerüljek?": "Does increasing my contribution improve my chances of being selected?",
    "Mi történik a részvételi összegemmel, ha a kijelölt lejárati idő letelik, de nem gyűlt össze a célár?": "What happens to my contribution if the goal isn't reached before expiration?",
    "Mi történik a részvételi összegemmel, ha a kijelölt lejárati időn belül sikerült összegyűjteni a célárat, de nem én lettem a szerencsés kiválasztott?": "What happens to my contribution if the goal is met but I am not selected?",
    "Hogyan tudom beváltani a levásárolható kedvezményeimet?": "How can I redeem my shopping discount credits?",
    "Fizethetem egy termék árát 100%-ban csak levásárolható kedvezményből a Store-oldalon?": "Can I pay 100% of an item using discounts in the Store?",
    "Van lehetőség a levásárolható kedvezményt ismét Indollárra váltani?": "Is it possible to convert shopping discounts back into Indollars?",
    "Mi az az Auto-in funkció?": "What is the Auto-in feature?",
    "Mi az az Indollar?": "What is an Indollar?",
    "Hogyan szerezhető Indollar?": "How do I acquire Indollars?",
    "Meghívóval járó ajándék feltöltéshez hogyan lehet hozzájutni?": "How do I claim invite bonus credits?",
    "Mi a Space a menüben?": "What is 'Space' in the menu?",
    "Hogyan tudom elősegíteni a termékek árának összedobását?": "How can I help complete a product's funding?",
    "Hogyan csatlakozhatom az influenszerekhez, és mi történik utána?": "How do I join an influencer's team, and what happens next?",
    "Influenszerként szeretnék profilt készíteni, mi a teendőm?": "I am an influencer and want to create a profile, what should I do?",
    "Bárki kínálhat eladásra terméket a SocialStore platformon?": "Can anyone list products for sale on SocialStore?",
    "Honnan érkeznek a megvásárolt vagy közösen összedobott termékek?": "Where are purchased or funded products shipped from?",
    "Vásárlóként tudok terméket vagy szolgáltatást javasolni a platformra?": "As a customer, can I suggest products or services for the platform?",
    "Rendelkeznek garanciával a termékek?": "Do items carry a warranty?",
    "Hol kell érvényesíteni a garanciát, vagy esetleges panaszt?": "Where do I file warranty claims or customer service requests?",
    "Hol tudom a kiszállítási címem módosítani?": "Where can I update my shipping address?",
    "Hol tudom nyomon követni a megvásárolt vagy sikeresen összedobott termékem státuszát?": "Where can I track the shipping status of my order?",
    "Termék cseréjére van lehetőség?": "Are product replacements or exchanges supported?",
    "Minden termék esetén ingyenes a kiszállítás?": "Is shipping free on all items?",
    "Minden országba ingyenes a kiszállítás?": "Is international shipping free to all countries?",
    "Profilt regisztráltam, de a konfirmáló e-mail nem érkezett meg.": "I registered, but didn't receive the confirmation email.",
    "Nem tudok belépni a fiókomba, mit tegyek?": "I can't log in to my account, what should I do?",
    "Elfelejtettem a jelszavam, mit tegyek?": "I forgot my password, what should I do?",
    "Véletlenül szálltam be egy termék közösségi vásárlásába. Mit tegyek?": "I joined a group purchase by mistake. What can I do?",
    "Hogyan tudom törölni a profilomat?": "How do I delete my profile?",
    "Mi történik az egyenlegemmel, ha törlöm a profilomat?": "What happens to my balance if I delete my profile?",
    "Kérdésed van?": "Have questions?",
    "írj nekünk!": "Contact us!"
}

def run():
    hu_root = 'hu'
    en_root = 'en'

    if not os.path.exists(hu_root):
        print(f"Hiba: '{hu_root}' mappa nem található!")
        return

    # 1. Magyar oldalakon a placeholder.html lecserélése a leendő en megfelelőre
    for root, _, files in os.walk(hu_root):
        for f in files:
            if f.endswith('.html'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    data = fp.read()
                
                # Zászló link javítása: placeholder helyett a fooldal en verziója
                data = data.replace('placeholder.html', '../../en/fooldal/index.html')
                data = re.sub(r'href=["\'][^"\']*placeholder\.html["\']', 'href="../../en/fooldal/index.html"', data)
                
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(data)

    print("Magyar oldalak nyelvváltó linkjei kijavítva.")

    # 2. 'en' mappa létrehozása a hu mintájára
    if os.path.exists(en_root):
        shutil.rmtree(en_root)
    shutil.copytree(hu_root, en_root)

    # 3. placeholder.html törlése az en mappából, ha átmásolódott
    ph_en = os.path.join(en_root, 'fooldal', 'placeholder.html')
    if os.path.exists(ph_en):
        os.remove(ph_en)

    # 4. Angol fájlok fordítása és visszairányítása hu-ra
    for root, _, files in os.walk(en_root):
        for f in files:
            if f.endswith('.html'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    data = fp.read()

                # Szövegcsere
                for hu_text, en_text in translations.items():
                    data = data.replace(hu_text, en_text)

                # HTML lang attribútum átírása
                data = data.replace('lang="hu"', 'lang="en"').replace('lang="hu-HU"', 'lang="en-US"')

                # Navigációs linkek átírása en-re az en oldalakon belül
                data = data.replace('/hu/', '/en/')

                # Zászló linkje az angol oldalon: mutasson vissza a magyar megfelelőre
                data = data.replace('../../en/fooldal/index.html', '../../hu/fooldal/index.html')

                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(data)

    print("Angol verzió ('en/') sikeresen legenerálva és lefordítva!")

if __name__ == '__main__':
    run()