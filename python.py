from time import sleep
q = 0
z = 0
i = 50
print("ця історія про фею дінь дінь")
print(" Глава 1.вона народилася в маленькому селищі але її батьки померли")
print("одного дня королева людського світу пішла в похід та натрапила на маленьку дінь дінь та вирішила забрати її з собою")
print("у королеви було дві дочки яким не сподобалась дінь дінь з самого початку")
i = i+10
print("Вітаю з проходженням 1 глави. В тебе є " + str(i) + " кристалів")
sleep(7)
print("ГЛАВА 2.")
print("Через 14 років")
print("Брунгільда: бож дінь дінь така кринжова і чому вона наша сестра? ")
print(" Зельда:згодна але ж мама її обожнює")
print("дінь дінь йшла і почула як дівчата говорять")
k = input("що зробити? піти далі/ підслухати{10 кр}")
sleep(3)
if k == "піти далі":
    print("ти пішла і вирішила не підслуховувати")
    print(" ти пішла на обід. На обіді ти завжди сидиш біля мами королеви та ви просто говорили про домашні справи та що плануємо робити.")

if k == "підслухати":
    i = i-10
    print("В тебе залишилося " + str(i) + " кристалів")
    print(" ти слухаєш їхню розмову далі")
    print("Брунгільда: але ж по ній видно що вона не нашого роду")
    sleep(3)
    print("Зельда: цікаво вона досі думає що одна із нас?")
    sleep(3)
    print("розмова закінчилася ти пішла далі")
    sleep(3)
    print("ти пішла на обід. На обіді ти завжди сиділа біля мами королеви тому ти могла з нею поговорити про те що почула від дівчат")
    print("ти: мамо а чому я не схожа на вас?(пошепки питаєш)")
    sleep(3)
    print("мама: тому що ти особлива сонечка. Люблю тебе - пошепки каже")
    sleep(3)
    print("ця розмова тобі не особливо допомогла ")
print("після обіду ти пішла в сад прогулятися.Сад був з видом на ліс. Ти сиділи читала книгу аж раптом ти почула якісь шорохи і потім побачила дорослого оленя але такого ж маленького як і ти. І з цього моменту ти зрозуміла що ти не одна і вночі вирішила полетіти в ліс та знайти свою справжню родину.")
i = i + 10
print("Вітаю з проходженням 2 глави. В тебе є " + str(i) + " кристалів")
sleep(3)
print("ГЛАВА 3.")
sleep(3)
print("ніч: ти вилітаєш зі свого прекрасного будинку в якому в тебе було все і вирішуєш полетіти в ліс де тобі все невідоме")
print("ти заблудилася в лісі ти сидиш під деревом та мерзнеш. Але з часом до тебе підбігає олень і тобі здається що це той якого ти бачила вдень.")
sleep(3)
h = input("що робити? роздивлюватися його{10кр} /злякатися")
if h == "роздивлюватися його":
    q = q+1
    i = i-10
    print("ти зацікавила його і в нього з'явилося бажання допомогти тобі")
if h == "злякатися":
    print("він допоможе тобі")
sleep(3)
print("І тут олень перетворюється в доросло чоловіка але зростом трохи вище дінь дінь")
sleep(3)
print("олень: привіт що сталося? Чому ти не вдома?")
sleep(3)
print("ти вже хотіла відповісти на перше питання але тебе зацікавило друге(і звідки він знає де мій дім? можливо той олень і був він?) багато запитань було в твоїй голові але жодної відповіді")
if h == "роздивлюватися його":
    print(" Олень:якщо чесно тільки не лякайся. Я приходив до вашого замку декілька разів думаю ти і сама знаєш")
    print("посміхаться він")
if h == "злякатися":
    print("Олень: просто здогадвся зазвичай такі дівчатка як ти мають дім")
    sleep(3)
print("Олень: що тебе турбує? Чому ти тут одна?")
sleep(3)
print("Ти: я не схожа на свою родину тому вирішила знайти свою справжню родину")
sleep(3)
print(" Олень:Тобі дуже пощастило що ти зустріла мене бо мені здається я знаю де це")
sleep(3)
print("Олень: ти підеш зі мною?")
sleep(3)
a = input("піти з ним? так{10}/ ні")
if a == "так":
    q = q+1
    i = i-10
    print("він перетворюється на оленя та каже сідати на нього та їхати на ньому. Ти сідаєш та їдеш.")
    sleep(3)
    print("Ви приїхали в поселення з маленькими будинками і він повів тебе до одної дівчини. По його словах це його давня знайома тому я можу переночувати в неї бо за вікном ніч")
    sleep(3)
    print("Олень: дінь дінь це Стейла. Стейла це дінь дінь")
    sleep(2)
    d = input("Привітатися з стейлою? так{10} /ні")
    if d == "так":
        i = i-10
        print("чудово, в тебе можливо будуть друзі. Але посплілкуєтесь про завтра")
        print("ти лягла спати")
    if d == "ні":
        print("вона вирішила що ти не дуже доброзичлива")
        print("ти лягла спати")
if a == "ні":
    print("Олень: ну як хочеш, я пішов")
    print("ти залишилася ночувати в лісі, а на ранок ледве знайшла поселення і всеодно невпевнена чи це воно")
    print("тому підійшла до дівчини і вирішила запитати в неї")
    sleep(4)
    r = input("Привітатися з нею? так{10} /ні")
    if r == "так":
        i = i-10
        print("вона розповіла , що її звати Стейла і розповіла все що ти хотіла")
        print("здається ви подружилися")
        sleep(3)
    if r == "ні":
        print("ти здалася не дружелюбною, але вона неохоче розповіла")
        print("здається ти ніколи не знайдеш друзів")
        sleep(3)
print("Минула ніч ти прокинулася зранку")
i = i+10
print("Вітаю з проходженням 3 глави. В тебе є " + str(i) + " кристалів")
print("ГЛАВА 4")
if a == "так":
    if d == "так":
        print("ти можеш поговорити з Стейлою")
        print("Ти прокинулася зранку")
        print("Ти: привіт, Стейло. А звідки ти знаєш оленя?")
        print("Стейла: його звати не олень, а Майк. Ми з ним виросли разом можна вважати. А тобі що? Закохалася?")
        print("Ти: мені просто цікаво хто мене врятував. Але добре.")
        sleep(5)
        if a == "ні":
            print("Ти гуляєш вулицями та шукаєш собі знайомих")
else:
    print("ти не можеш поговорити з Стейлою")
    sleep(2)
print("Стейла: я маю справи, хочеш зі мною?")
print("Ти: так звісно пішли")
sleep(3)
print("ви пішли в місто та зустріли там друга Стейли Байрона. Він був симпатичним хлопцем і зразу тобі сподобався")
print("ви зразу знайшли з ним спільну мову і прекрасно провили час. Він запросив тебе прогулятися і ти згодилась")
sleep(3)
print("черезе деякий час:")
print("ви прогулюєтесь біля величезного моря хоча для людей це маленька річка")
print("Байрон: як ти сюди потрапила?")
sleep(3)
o = input("сказати правду{10} /збрехати")
if o == "сказати правду":
    z = z+1
    i = i-10
    print("ти сказала правду і ваші відносини покращилися")
if o == "збрехати":
    print("ти не дуже довіряєш йому, але можливо з часом все стане краще")
sleep(5)
print("ви ще трохи прогулялися і пішли до дому")
print("ти поки що живеш у стейли, але дуже хочеш свій будинок")
sleep(2)
print("ввчері до тебе приходить Стейла і каже, що її селищу потрібна допомога")
print("Стейла: потрібно зварити зіл'я для потреб селища. З коріня мандагори та квіткою життя, але є одна проблема всі хто вміє варити ці зіл'я поїхали в експедицію")
sleep(2)
e = input("допомогти зварити зіл'я? так{10}/ ні")
if e == "так":
    i = i-10
    print("ти допоможеш зварити зіл'я і допоможеш селищу вони це запам'ятають")
    print("Стейла: справді? Велика дякую, але тобі потрібно знайти квітку життя. Надіюсь ти справишся. Піду всім розкажу")
    sleep(3)
if e == "ні":
    print("ти не допоможеш")
    print("Але стейла сказала що можливо байрон погодиться")
print("ти вирішила знову зустрітися з Байроном")
i =i+10
print("Вітаю з проходженням 4 глави. В тебе є " + str(i) + " кристалів")
print("ГЛАВА 5")
if e == "так":
    print("Наступного дня Дінь дінь зустрілася з Байроном.Він розповів їй про його походження,а саме про те ,що його бабуся була травницею.")
    print("Як сказав Байрон в його бабусі була книга про різні рослини,їхні властивості та де їх знайти.")
    sleep(2)
if e == "ні":
    print("байрон сказав що хоче піти за другим копмонентом зіл'я і ти запропонувала піти разом")
print("Отже,вони відправились на пошуки тої самої квітки.")
print("Байрон: в книзі бабусі написано,що ця квітка росте в самих чащах темного лісу.")
sleep(2)
print("Дінь дінь:отже туди й відправимось,нам страхи не страшні")
print("На цьому їхній діалог не продовжувався доки  вони вже були на половині дороги вони  зустріли несподіваного гостя.")
print("Майк:Ого що це ви тут робите в цьому лісі?Тут небезпечно.")
sleep(2)
print("Вони привітались,Майк та Байрон обмінялись ехидними посмішками.")
print("Дінь дінь:Ми тут по одній справі")
sleep(2)
print("Майк подумав і вирішив,що не довіряє Байрону,та залишати його з Дінь дінь не можна.")
print("Майк:Ну то я з вами піду,допоможу якщо що.")
sleep(2)
p = input("Погодитися{10} /відмовитися")
if p == "погодитися":
    i = i-10
    q = q+1
    print("Дінь дінь:Ну добре,можеш йти з нами.")
    print("Байрону не сподобалось,що Майк буде йти з ними,аде він промовчав.І вони продовжили йти далі.")
    print("Майк:То що в вас за справа?")
    sleep(3)
    print("Дінь дінь:Ми шукаємо особливу квітку.")
    print("Майк:А як ця квітка виглядає?")
    sleep(2)
    print("Байрон:Ооо ви ошаленієте коли побачите її,вона дуже гарна.")
    print("Ця квітка проростає лише в один день в році - в повний місяць.Її пелюстки схожі на відблиск сонця на водній гладі,а стовбур вкритий гострими шипами.")
    print("Вони пройшли так ще десь з годину та вирішили зробити перевал.")
    print("Запалити костер,щоб нічний ліс не був особливо жорстокий з ними,та трохи поспати.Майк запалив костер та компанія сіла погрітись.")
    y = input("З ким сісти? Майком{10} /Байроном{10}")
    if y == "Майком":
        q = q+1
        i = i-10
        print("Дінь дінь вирішила,що їй буде комфортніше поруч з Майком.")
        print("Дінь дінь:Гей,можна я тут присяду?")
        sleep(2)
        print(" Майк:Ну звичайно,я тільки за.")
        print("Дінь дінь:Я хотіла поговорити з тобою,чому ти вирішив піти з нами?")
        print(" Майк: я не міг залишити тебе з цим незнайомцем.")
        sleep(2)
        print("Дінь дінь:то для тебе він незнайомець,а я його знаю.")
        print(" Майк:ну то що?Я ж захищаю тебе,поки я тут ти можеш спати спокійно,засипай.")
        print("Дінь дінь заснула.")
        sleep(2)
    if y =="Байроном":
        z = z+1
        i = i-10
        print("Дінь дінь вирішила ,що з ним їй буде комфортніше.")
        print(" Дінь дінь:Я пiдсяду?")
        print(" Байрон:Звичайно,сідай.")
        sleep(2)
        print("Він трохи посунувся щоб їй було більше місця.")
        print("Байрон:І давно ти з ним знайома?")
        sleep(2)
        print("Дінь дінь:Не сильно довше аніж з тобою.")
        print("Байрон:Хах,справедливо.Але він мені не подобається.")
        sleep(2)
        print("Дінь дінь:Чому це?")
        print(" Байрон:Бо він олень,відчуваю його напищену енергетику.")
        sleep(2)
        print("  Байрон:Але не важливо,лягай спати,ти в безпеці.")
        print("Дінь дінь заснула.")
        sleep(2)
if p == "відмовитися":
    print(" Дінь дінь:Ні,дякую,ми впораємось самі.")
    print("Майк пішов,а Дінь дінь і Байрон знову залишились на одинці.")
    sleep(2)
    print("Байрон зрадів,що Mайк не пішов з ним,він йому не сподобався.")
    print("Вони продовжили йти далі.")
    sleep(2)
    print("Дінь дінь:Байроне,а можеш будь ласка описати,як виглядає ця квітка?")
    print(" Байрон:Вона дуже гарна.")
    sleep(2)
    print("Ця квітка проростає лише в один день в році - в повний місяць.Її пелюстки схожі на відблиск сонця на водній гладі,а стовбур вкритий гострими шипами.")
    print(" Дінь дінь:Я ще не бачила,але опис звучить дуже багатообіцяючи.")
    sleep(2)
    print("Вони пройшли так ще десь з годину та вирішили зробити перевал.")
    print("Запалити костер,щоб нічний ліс не був особливо жорстокий з ними,та трохи поспати.")
    sleep(2)
    print("Байрон запалив костер та вони сіли погрітись.")
    w = input("Сісти поруч з Байроном чи далі? поруч{10} /далі")
    sleep(2)
    if w == "поруч":
        z = z+1
        i = i-10
        print("Дінь дінь вирішила ,що могла б трохи поговорити з ним перед сном.")
        print("Дінь дінь:Я підсяду?")
        sleep(2)
        print("Байрон:Звичайно,сідай.")
        print("Він трохи ссунувся  щоб їй було більше місця.")
        sleep(2)
        print("Дінь дінь:Я хочу подякувати,за те що ти допомагаєш мені знайти цю квітку.")
        print("Байрон:Не треба подяки,радий допомогти міледі.")
        sleep(2)
        print("Дінь дінь:Ти дуже добрий,з тобою приємно вести розмову.")
        print("Байрон:Я не з усіма такий,май на увазі.")
        sleep(2)
        print(" Байрон:Тобі потрібно більше сил,лягай спати,я охороняю твій сон.")
        print("Дінь дінь заснула.")
        sleep(2)
        if w == "далі":
            print("Дінь дінь вирішила не напружувати Байрона розмовою.")
            print("Вона трохи посиділа,погрілась та заснула.")
print("МАЙК НЕ ПІШОВ З НИМИ Почався ранок,вони зібрались та пішли далі.")
print("Через трохи часу вони побачили неймовірної краси галявину,яка й була їхньою ціллю.")
print("Дінь дінь:Яка краса,це і є це місце?")
print("Байрон:Так,це те місце яке ми шукали.")
print("Дінь дінь:А он де квітка!")
print("Вони й не помітили де саме вони стоять,адже квітка знаходилась на пласкій поверхні льоду вкритого легким пушком.Це було схоже на звичайну галявину тож вони й гадки не мали...")
print("Дінь дінь в захваті від того ,що вона майже дісталась до того що вони шукали побігла до квітки,доки лід під нею тріскався.")
print("Байрон:зупинись Дінь дінь!!!")
print("Але було вже пізно.Лід під Дінь дінь тріснув,та вона провалилась в прозору безодню.")
i = i+1
print("Вітаю з проходженням 5 глави. В тебе є " + str(i) + " кристалів")
print("Ваш зв'язок з Майком " + str(q) + " сердець")
print("Ваш зв'язок з Байроном " + str(z) + " сердець")
print("ГЛАВА 6")
print("Поки ще була в свідомості Дінь дінь боролась з темною пеленою заснилаючою її розум,і в останній момент як вона ще не відключилась вона побачила як до неї тянеться чиясь рука.")
print("Дінь дінь спробувала дотянутись до неї,але не вийшло,вона втратила свідомість.")
print("Рука дотянулась до неї,схопила її  та почала витягувати на поверхність.")
lk = input("Це був... Майк{10} /Байрон{10}")
if lk == "Майк":
    i = i-10
    q = q+1
    print("")
if lk == "Байрон":
    i = i-10
    z = z+1
    print("")
print("Прокинувшись Дінь дінь оглянулась навколо.")
print("Дінь дінь:{Де це я?}")
print("Подумала вона")
print("Вона знаходилась в милій кімнатці в чиємусь будинку.Дівчина спробувала встати з ліжка та головна біль дала про себе знати,в неї паморочилась голова.В цей момент в кімнату зайшов...")
po = input("Майк{10}/ Байрон{10}")
sleep(3)
if po == "Майк":
    i = i-10
    q = q+1
    print("")
    if q >= 3:
        print("При прокачаних відносинах доступна ця сцена.")
        print(" Майк:Дінь дінь,тобі не слід було вставати з ліжка")
        sleep(3)
        print("Він підбіг до неї та допоміг їй сісти назад.")
        print(" Дінь дінь:Майк?Як ти тут опинився?")
        print("Майк:не важливо як,важливо,що як тільки я відходжу від тебе ти створюєш собі проблеми,ну як мала дитина їй богу.")
        print(" Дінь дінь:Я як мала дитина?!Та йди ти.")
        sleep(3)
        print("Майк:ну не ображайся,я ж любя.")
        print("Сказавши це Майк клацнув Дінь дінь по носу. Дінь дінь вскочила і вдарила його")
        print("Майк:Я ж сказав,як мала дитина.")
        sleep(3)
        print("Майк схопив її за руку,посадив собі на коліна та міцно обійняв її.")
        print("Дінь дінь:Що ти робиш?..")
        print("Майк:Я дуже переживав за тебе,давай ти потім вимістиш свій гнів,а зараз просто трохи посидимо в тиші.")
        print("Ще кілька хвилин вони так посиділи,а потім вирішили вийти з кімнати.")
if po == "Байрон":
    i = i-10
    z = z+1
    print("")
    if z >= 2:
        print("По прокачаним відносинам з Байроном доступна ця сцена.")
        print("Байрон вирішив перевірити як там Дінь дінь.Він зайшов в кімнату та побачив ,що вона вже прокинулась.")
        print(" Байрон:Омг Дінь дінь,ти як?")
        sleep(3)
        print("Байрон:Як добре що ти жива")
        print(" Дінь дінь:Трохи голова паморочиться,але в цілому все добре.")
        print("Байрон:радий чути.")
        sleep(3)
        print("Дінь дінь:А що це за місце?")
        print(" Байрон:Коли я витягнув тебе з води,ти була непритомна,я думав ,що ти не вижевеш,але не втрачав надії,я взяв тебе на руки та ми з Майком почали пробиратись через ліс.")
        print(" Байрон:Незабаром ми побачили клубок диму проходящий понад деревами.")
        print("Байрон:І ми пішли по його слідам,так ми дійшли до цього селища.")
        sleep(3)
        print("Байрон:Побачивши як двоє людей виходять з лісу,а потім ще й помітивши непритомну дівчину на руках одного з них до нас підбігла стара жінка.")
        print("Байрон:Вона сказала нести тебе в її дім,виділила кімнату.")
        print("Закінчивши розповідь він подивився на реакцію Дінь дінь.")
        print("Дінь дінь:Який жах,зачекай а звідки там з'явився Майк?")
        sleep(3)
        if q >= 3:
            print("Байрон:Він вибіг з лісу як тільки побачив як ти провалилась.")
        else:
            print("не знаю")
            print("Вони ще трохи поспілкувались не о чем і вирішили вийти з кімнати.")
            sleep(3)
print("Вітаю з проходженням 6 глави. В тебе є " + str(i) + " кристалів")
print("Ваш зв'язок з Майком " + str(q) + " сердець")
print("Ваш зв'язок з Байроном " + str(z) + " сердець")
print("ГЛАВА 7")
print("Вони вийшли з кімнати ,Дінь дінь одразу устромила свій погляд на незнайому їй жінку.")
print("Дінь дінь:{Певне це ця жінка,яка приютила нас. }")
print("Жінка:Ой дитино,як добре, шо ти прокинулась, тримай ось,настоєчку.")
print("Жінка:Ця настоянка допоможе тобі з головною болю.")
print("Дінь дінь сіла за стіл . Вона взяла з рук Жінки чашу , але не поспішала пити.")
print("Подумала: {Що воно таке?}")
print("Жінка:Та ти пий, не бійся,не отруєна.")
print("Дінь дінь вирішила, що жінці нема чого труїти її та все ж випила настоянку.Жінка трохи подумавши за щось своє через пару хвилин принесла кілька тарілок їжи та щось попити.")
print("Дінь дінь:Дякую вам велике, за вашу доброту")
print("Жінка:Та не дякуй дитино, мені тільки в радість про когось попіклуватись.")
print("Після того як Дінь дінь закінчила з трапезою жінка запропонувала Дінь дінь прогулятись по селищу щоб трохи розвіятись.Хлопці підтримали цю ідею і вони разом, вже трохи більш дружною компанією пішли на вулицю.")
print("Вийшовши з хати першим ділом Дінь дінь довелось замружити очі від сильно світившого сонця.А одразу після того як вона їх відкрила ахнути від краси цього села.")
print("Навколо були гарно побудовані дерев’яні будиночки нагадавши їй грибочки.Коло них пробіг гурт дітей весело граючих в доганяли.А найдивовижнішим був великий дуб,здоровезний . Дінь дінь поглянула на сходи ведучі на вершину цього дуба.")
print("Подумала: {Невже там теж хтось живе?!}")
print("Байрон:Я розділяю твоє захоплення.")
print("Байрон:Тут справді чарівно.")
print("Щойно згадавши щось неймовірно важливе він сказав друзям , що зараз повернеться, а сам побіг в сторону будинку з якого вони щойно вийшли.А повернувся він тримаючи руки за спиною.")
print("Байрон:Дінь дінь, вгадай-но що в мене в руці.")
print("Дінь дінь:Як же я можу вгадати?Просто покажи,що там?")
print("Вона спробувала обійти хлопця,але їй це не вдалося.І тоді Дінь дінь вирішила:")
m = input("Обійняти{10} /нічого")
if m == "Обійняти":
    i = i-10
    z = z+1
    print("Байрон здивувався,він не очікував,що дівчина його обійме,але йому було приємно.")
    print("А Дінь дінь в той час коли хлопець був спантеличений вихватила річ в нього з руки.")
    print("Дінь дінь:Що тут у нас.")