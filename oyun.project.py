class oyun_motoru:
    def __init__(self):
        self.durum = "başlangıç"

    def başlat(self):
        print("Hoş Geldiniz!\nBu Sezer adlı bir adamın hikayesidir.\nSezer'in hayatı basitti.\nHer sabah yatağından kalkıp sıkıcı işine gider,ailesini geçindirebilmek için bütün gün çalışırdı. ")
        print("Sessiz biri olduğu için pek arkadaşıda yoktu.\nOnun için önemli olan sadece 2 şey vardı: İşi ve Ailesi.\nVe Sezer.. Mutluydu.\n \nAma bir sabah çok garip bir şey oldu.\nSezerin hayatını tamamen değiştirecek bir şey.")
        print("Sabah uyandığında kuru bir sessizlik vardı,ne bir araba ne de bir insan sesi.Sezer ailesini görmek için odadan çıktı ama ev boştu.\nTelevizyonu açtığında hiç bir kanal göstermiyordu ve kimse telefonunu açmıyordu.\nSezer hızlıca dışarı çıktı.\nKoca mahalle bomboştu.Tüm herkes neredeydi?\nSezer belki birilerini görürüm diye şehir merkezine gidecekken karşı evden gelen ses dikkatini çekti.  ")
        self.oyun_devam()

    def oyun_devam(self):
        while self.durum != "son":
            if self.durum == "başlangıç":
                self.başlangıç()
            elif self.durum == "karşıdaki_ev":
                self.karşıdaki_ev()
            elif self.durum == "bodrum":
                self.bodrum()
            elif self.durum == "şehir_merkezi":
                self.şehir_merkezi()
            elif self.durum == "son":
                self.son()
            elif self.durum == "otogar":
                self.otogar()
            elif self.durum == "bodrum2":
                self.bodrum2()
            elif self.durum == "terminal":
                self.terminal()
            elif self.durum == "kilit":
                self.kilit()
            elif self.durum == "savunma":
                self.savunma()
            elif self.durum == "hotel":
                self.hotel()
            elif self.durum == "oda101":
                self.oda101()
            elif self.durum == "arka_kapı":
                self.arka_kapı()
            elif self.durum == "aile":
                self.aile()
            else:
                print("Geçersiz durum! ")
                break



    def başlangıç(self):
        print("\nNe yapmak istersin? ")
        print("1: Şehir merkezine doğru git.")
        print("2: Karşıdaki eve doğru git.")
        seçim = self.seçim_yap(["1","2"])
        if seçim == "1":
            self.durum = "şehir_merkezi"
        elif seçim == "2":
            self.durum = "karşıdaki_ev"

    def karşıdaki_ev(self):
        print("\nSezer karşıdaki eve doğru gitti.\nSes giderek artıyordu.\nBirisini bulma umuduyla önündeki odaya ilerledi.\nİçeride kendisini açık bir televizyondan başka bir şey karşılamadı.Nerede bu insanlar?\nSezer kafayı mı yiyorum diye düşünürken masadaki not dikkatini çekti.\n")
        print("Hey Mete,\nSaat 5'te otogara gel. Dün gece hiçbir şey iyi gitmedi,bodrumdaki eşyaları getirmeyi sakın unutma.\nBunu başarabiliriz...\n ")
        print("\nNe yapmak istersin? ")
        print("1: Otogara git.")
        print("2: Bodruma git.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "otogar"
        elif seçim == "2":
            self.durum = "bodrum"

    def bodrum(self):
        print("\nSezer hızlı kalp atışlarıyla beraber merdivenlerden inerken kuru bir karanlığa doğru gittiğini farkeder.Aynı zamanda bodrumdan garip sesler duymaya başlar.\nİner,iner ve bodrum kapısını görür.\nAma kapı maalesef kilitlenmiştir.Sezer belkide her şeye burnumu sokmasam iyi olur diye düşünür.")
        print("\nNe yapmak istersin?")
        print("1: Otogara git.")
        print("2: Etrafı araştırmaya başla.")
        seçim = self.seçim_yap(["1","2"])
        if seçim == "1":
            self.durum = "otogar"
        elif seçim == "2":
            self.durum = "bodrum2"

    def şehir_merkezi(self):
        print("\nSokaklar bomboştu.Her yer ürpertici bir sessizliğe bürünmüşken yumuşak bir yağmur yağmaya başladı.\nSezer daha önce hiç bu kadar yalnız hissetmemişti.\nVe şehir merkezi,kimse yok.Sezer sinirden aklını kaybetmek üzereydi.Düşün,düşün,düşün...")
        print("Sezer derin düşüncelere dalmışken bir tehlike sezdi.Uzaktan kendisine doğru koşan bir şey vardı.Dikkatli bir şekilde baktı ve..\nBu bir kurttu.\nSezer korkudan dona kalmıştı.Ne yapacağını bilmiyordu.")
        print("\nNe yapacaksın?")
        print("1: Kaçmayı dene!")
        print("2: Kendini savun!")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "hotel"
        elif seçim == "2":
            self.durum = "savunma"


    def otogar(self):
        print("\nSezer yola koyuldu.Sokaklar bomboştu.\nSezer yavaş adımlarla otogara doğru giderken bir yandan notun ne anlama geldiğini düşünüyordu.Ve sonunda vardı\nHer gün binlerce kişinin bulunduğu otogar tamamen bomboştu.\nBunların anlamı ne Sezer'in artık bazı cevaplar bulması gerekiyordu.")
        print("\nNe yapmak istersin?")
        print("1: Terminale gir.")
        print("2: Şehir merkezine doğru git.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "terminal"
        elif seçim == "2":
            self.durum = "şehir_merkezi"



    def bodrum2(self):
        print("\nSezer cidden mi? herkes kaybolmuş ortada büyük bir gizem var ve sen kapıyı mı açmak istiyorsun?\nNeyse.. Pekala soldaki balyoz Sezerin dikkatini çeker.Belki bununla kapıyı kırabilirim diye düşünür.\nEline alır ve tüm gücüyle..BOOOMM.\nKapıdan içeri girer ama o da ne,\ntam karşıdaki duvarda kapıyla beraber sensörlü,kurulmuş bir arbalet; üstelik tamda sana doğru geliyor. ")
        print("Ve evet maalesef Sezer kendisine gelen bir ok yüzünden kan kaybından orada ölüyor.\nBelkide bu kadar fazla meraklı olmasaydı içinde olduğu bu gizemi çözebilirdi.")
        print("\nEğer evden ilk çıktığın andan başlamak istersen lütfen 1 e bas.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "başlangıç"
        else:
            print("1'e basmadığınız için oyun sonlandırılıyor.")
            self.durum = "son"


    def terminal(self):
        print("\nSezer elindeki nota güvenerek hızlıca terminale girdi.\nBoş koltuklar dışında ortada hiçbir şey yoktu.Sezer'in artık bazı cevaplar bulması gerekiyordu.\nVe öğrenmenin tek bir yolu vardı.\nSezer kamera kayıtlarının bulunduğu kilitli kapının önündeydi.Sezer istersen şehir merkezine hala gidebiliriz.")
        print("\nNe yapmak istersin?")
        print("1: Kilidi açmaya çalış.")
        print("2: Şehir merkezine doğru git.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "kilit"
        elif seçim == "2":
            self.durum = "şehir_merkezi"
    def kilit(self):
        print("\nTamam Sezer.Şimdi tek yapmamız gereken kilidi bulm.. Eeee.. Sezer? O maymuncuk sende ne arıyor? Pekala.\nSezer soğuk kanlılıkla içeri girer.Artık zamanı gelmişti.Bütün cevaplar bu sabahki kamera kayıtlarındaydı.\nVe Sezer düğmeye bastı..\nŞimdi.. Bu dosyalar nerde? (Kamera kayıtları bulunamıyor) Bir sorun olmalı.\nBir dakika burda başka bir dosya daha var ve içinde şöyle yazıyor:\n\nUnutma Furkan, 04.07.2024 tarihinde saat 16:00'a kadar ŞEHİR MERKEZİNE GİTMELİSİN.. Yoksa sende otogarla beraber havaya uçarsın.")
        print("\nSezer bu mesajı görünce saatine baktı ve saat 15:58'i gösteriyordu.\nDaha yazının neyden bahsettiğini anlayamadan masanın altında,koridorda,diğer odalarda ve kısacası otogarın heryerinde\nkırmızı ışıkla beraber ses çıkararak yanan bombaları farketti.\n2 dakikada otogardan çıkması imkansızdı.Ağlayarak bildiği tüm duaları okumaya başladı ve sonra\nBOOOMM..\nKaçınılmaz son artık gelmişti.\nBelkide bu kadar fazla meraklı olmasaydı bu kilitli odaya hiç girmeyip içinde olduğu bu gizemi çözmeye gidebilirdi.")
        print("\nEğer evden ilk çıktığın andan başlamak istersen lütfen 1 e bas.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "başlangıç"
        else:
            print("1'e basmadığınız için oyun sonlandırılıyor.")
            self.durum = "son"

    def hotel(self):
        print("\nKoş Sezer kooşşş! Hadi yaklaşıyor! Sezer sağa dön bu binaya girebiliriz!\nTamam,burada güvendeyiz.Kurt buraya giremez.Şimdi ışığı bulmamız lazım.\nKurt hala kapıda.İnşallah bu binanın arka kapısı vardır.\nBir dakika şuan bir otelin lobisindeyiz.Peki bu 101 nolu odanın neden ışıkları yanıyor?")
        print("\nŞuan ne yapacaksın?")
        print("1: 101 nolu odaya git.")
        print("2: Arka kapıdan çık.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "oda101"
        elif seçim == "2":
            self.durum = "arka_kapı"

    def savunma(self):
        print("\nTamam Sezer,sakin ol tek yapman gereken zamanını iyi ayarlamak bunu başarabilirsin.\nSEZER HAYIRR..\n...\nSezer kanlar içinde yere düştü.\nYağmur damlalarını hala hissedebiliyorken ailesini düşündü.Herkesin kaybolduğunu.Neden kendisine bir şey olmadığını.\nNeden?? Ve Sezer bunları hiçbir zaman bilemeyecek... ")
        print("\nEğer evden ilk çıktığın andan başlamak istersen lütfen 1 e bas.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "başlangıç"
        else:
            print("1'e basmadığınız için oyun sonlandırılıyor.")
            self.durum = "son"

    def oda101(self):
        print("\nBu ışığın bir sebebi olmalı.Belki birisini bulabiliriz Sezer.Hazır mısın?\nSezer merdivenlere doğru yol aldı.Her bir adımda burnuna gelen garip koku artarken.Kalbi adeta yerinden çıkacaktı.\nSezerin artık son umuduydu.Ve sonunda 101 nolu odanın kapısına geldi.Ama bir dakika, kapıda ve yerde kanlar vardı.\nGerçekten içeri girmek istiyor musun?")
        print("1: İçeri gir.")
        print("2: Arka kapıdan çık.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "aile"
        elif seçim == "2":
            self.durum = "arka_kapı"

    def arka_kapı(self):
        print("\nSezer oradaki ışıkları önemsemeden arka kapıya doğru yöneldi.Karanlığın parlayan sokaklarında Sezer tek başına yürüyordu.\nNereye gittiğini bilmeksizin yürüyordu.101 nolu odada arkada bıraktıklarını düşünerek yürüyordu.\nBu düşünceler artık çığ gibi büyümüştü.Sezer ne yaparsa yapsın ailesine ulaşamayacağını düşünüyordu.\nArtık umudunu tamamen yitirmişti.\nBu yüzden yüksek bir tepeye çıkıp kendini ordan aşağı bıraktı.. ")
        print("\nEğer evden ilk çıktığın andan başlamak istersen lütfen 1 e bas.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "başlangıç"
        else:
            print("1'e basmadığınız için oyun sonlandırılıyor.")
            self.durum = "son"

    def aile(self):
        print("\nSezer titreyen eliyle kapıyı yavaşça açtı.\nSoğukkanlılıkla kana doğru yürüdü.\nVe karşısında ailesinin ölü bedenleri vardı.\nSezer çığlık atmaya başladı: Burada neler oluyor? Ben neden burdayım? Ailem neden burda? Ben kimiiiimmm?\nVe neticede Sezer kafayı yedi...")
        print("\nEğer evden ilk çıktığın andan başlamak istersen lütfen 1 e bas.")
        seçim = self.seçim_yap(["1", "2"])
        if seçim == "1":
            self.durum = "başlangıç"
        else:
            print("1'e basmadığınız için oyun sonlandırılıyor.")
            self.durum = "son"


    def seçim_yap(self, seçenekler):
        while True:
            seçim = input("Seçiminizi yapın: ")
            if seçim in seçenekler:
                return seçim
            else:
                print("Geçersiz seçim! Lütfen tekrar deneyin.")

    def son(self):
        print("son")


if __name__ == "__main__":
    oyun = oyun_motoru()
    oyun.başlat()

# Multiple choices leading to different outcomes