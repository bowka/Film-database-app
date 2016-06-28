from tkinter import *
from tkinter import ttk
import tkinter as tki
from tkinter import  filedialog
import tkinter.ttk as ttk
class pomoc(object):
    def __init__(self):
        self.help=Tk()
        self.help.title('HELP')
        self.help['bg']='#9E69D6'
        Label(self.help,text='Vitajte v aplikacii KINO FMFI. \n \n 1.zvolte nacitanie uz existujucej databazy stlacenim tlacitka "nacitaj Databazu". \n alebo \n 2. zvolte alternativu vytvorenia novej vasej sukromnej databazy. \n tak ze zadate nazov vaseho suboru a stlacite tlacitko "Uloz"' ,bg='salmon',fg='white',padx=30,pady=30).pack()
        Button(self.help,text='OK',font=('Helvetica',20),bg='#5A0DAC',command=(lambda:self.zavri()),fg='white',width=20).pack()
        
    def zavri(self):
        self.help.destroy()

class uvitacieOkno(object):
    def __init__(self,platno):
        platno["bg"]= "#28324E"
        platno.HELP = Button(platno,text= "POMOC",fg = "white",bg =  'Medium Purple',command=  (lambda: pomoc()),bitmap='question').grid(row=0,column=0,sticky=W)
        platno.QUIT = Button(platno,text= "KONIEC",fg= "white",bg=  'salmon',command=(lambda:self.zavri(platno))).grid(row=0,column=1,sticky=E+N+S)
        platno.nacitaj=Button(platno,text="nacitaj databazu",fg='white',bg='#5A0DAC',command=(lambda: zoznam.citaj(zoznam))).grid(row=1,column=0,columnspan=2, sticky=W+E+N+S,ipadx=50,ipady=30)
        platno.vytvor=Label(platno,text='nova databaza',fg='white',bg='#28324E').grid(row=2,column=0,columnspan=2, sticky=W+E+S,ipadx=50,ipady=30)
        platno.napis=Entry(platno,text='nova databaza')
        platno.get=Button(platno,text="vytvor",fg='#28324E',bg='Sky Blue',command=(lambda: self.tvorNovy(platno.napis.get())))
        platno.napis.grid(row=3,column=0,ipady=13)
        platno.get.grid(row=3,column=1,ipadx=30,ipady=10)
        
    def zavri(self,tk):#tlacidlo koniec zatvori appku
        tk.destroy()
    def tvorNovy(self,nazov):
        zoznam.vytvor(zoznam,nazov)
        

class Tabulka(object) :
    def __init__(self):
        self.main=[]
        
    def pridajFilm(self,film):
        self.main.append(film)
        
    def __str__(self):
        return str(self.main)

class zoznam():
    def __init__(self):
        self.nazov=''
        self.herci=''
        self.rok=''
        self.reziser=''
        self.obsah=''
        self.hodnotenie=''
    def citaj(self):
        f = filedialog.askopenfilename(filetypes =
                                       (("textove subory", "*.txt;")
                                       ,("odt subory", "*.odt"),
                                        ("All files", "*.*")))
        if f:
            t = open(f,'r')
            
            riadok=t.readline()
            tab = Tabulka()    
            while riadok!='': 
                riadok      =   riadok.strip().split('#')
                self.nazov  =   riadok[0]
                self.herci  =   riadok[1]
                self.rok    =   riadok[2]
                self.reziser=   riadok[3]
                self.obsah  =   riadok[4]
                self.hodnotenie=riadok[5]
                riadok      =   t.readline()        
                film=[self.nazov,self.herci,self.rok,self.reziser,self.obsah,self.hodnotenie]
                print(film)                
                tab.pridajFilm(film)
            root.destroy()#uvitacie okno zavri            
            Okno=HlavneOkno(tab,f)# otvori hlavne pracovne okno
        #----------------------------------------------------------------------------------------------------------------------------------------------------
    def vytvor(self,nazov_suboru):
##        t = open(nazov_suboru+'.txt', 'w')
        tab = Tabulka()
        root.destroy()#uvitacie okno zavri
        f = "{}.txt".format(nazov_suboru)
        Okno=HlavneOkno(tab,f)

        
class HlavneOkno(object):
    class Riadok(object):
        def __init__(self, id,  nazov = None, herci = None, rok = None, reziser = None, obsah = None,hod=None):
            self.id = id
            self.nazov = nazov
            self.herci = herci
            self.rok = rok
            self.reziser = reziser
            self.obsah = obsah
            self.hodnotenie=hod
    
    def __init__(self,tab,t=None):
        Hokno=Tk()
        save = PhotoImage(file="save.gif")
        edit = PhotoImage(file="edit.gif")
        delete = PhotoImage(file="delete.gif")
        new = PhotoImage(file="new.gif")
        Hokno.title('tabulka')
        Hokno['bg']='#380470'        
        self.tab=tab
        
        hlavicka=['nazov','herci','rok','reziser','obsah','hodnotenie']
        self.tree = ttk.Treeview(Hokno, columns=hlavicka, show="headings")
        self.tree.grid(row=1,column=0,columnspan=4)
        self.tree.heading('nazov',text='nazov')
        self.tree.heading('herci',text='herci')
        self.tree.heading('rok',text='rok')
        self.tree.heading('reziser',text='reziser')
        self.tree.heading('obsah',text='obsah')
        self.tree.heading('hodnotenie',text='hodnotenie')
        self.tree.bind("<ButtonRelease-1>",self.klik)
        
        Button(Hokno,text='pridaj',bg='#532881',command=(lambda:self.otvoredit()),image=new).grid(row=0,column=0)
        Button(Hokno,text='ZMAZ',bg='#532881',command=(lambda:self.zmaz(self.riadok)),image=delete).grid(row=0,column=1)
        Button(Hokno,text='edituj',bg='#532881',image=edit,command=(lambda: self.otvoredit(self.riadok, True))).grid(row=0,column=2)
        Button(Hokno,text='uloz',bg='#532881',command=(lambda : self.uloz(t)),image=save).grid(row=5,column=3)        
        Button(Hokno,text= "KONIEC",fg= "white",bg=  'salmon',command=lambda:self.zavri(Hokno)).grid(row=0,column=4)
        
        for i in range(len(tab.main)):
            self.tree.insert('','end',values=(self.tab.main[i][0],self.tab.main[i][1],self.tab.main[i][2],self.tab.main[i][3],self.tab.main[i][4],self.tab.main[i][5]),text=i)
        self.riadok = None
        
        vsb = Scrollbar(Hokno, orient="vertical",command=self.tree.yview)
        vsb.grid(row=1,column=5)
        self.tree.configure(yscrollcommand=vsb.set)
        Hokno.mainloop()

    def spravDict(self, tabPole):
        self.tab = dict()
        ix = 0
        for riadok in tabPole:
            self.tab[ix] = self.Riadok(ix, riadok[0], riadok[1], riadok[2], riadok[3], riadok[4],riadok[5])
            ix += 1
    def vypisDct(self):
        for riadok in self.tab:
            pass
        
    def zavri(self,pl):
        pl.destroy()
    def klik(self,e):
        itemClick = self.tree.focus()
        clickDict = self.tree.item(itemClick)
        if clickDict['text'] == '':
            return
        self.riadok = int(clickDict['text'])

        
    def zmaz(self,riadok):
        if self.riadok:
            self.tab.main.pop(int(riadok))
            self.tree.delete(*self.tree.get_children())
            for i in range(len(self.tab.main)):
                self.tree.insert('','end',values=(self.tab.main[i][0],self.tab.main[i][1],self.tab.main[i][2],self.tab.main[i][3],self.tab.main[i][4],self.tab.main[i][5]),text=i)
            
                
    def otvoredit(self, filmIx = None, edit = False):
        self.edit = Tk()
        self.edit.title('editacia')

        self.edit["bg"]= "#28324E"
        
        self.edit.nazov=Label(self.edit,text='nazov',fg='white',bg='#380470')
        self.edit.nazov.grid(row=0,column=0,sticky=W+E+N+S,ipadx=50,ipady=10)

        self.edit.herci=Label(self.edit,text='herci',fg='white',bg='#5A0DAC')
        self.edit.herci.grid(row=1,column=0,sticky=W+E+N+S,ipadx=55,ipady=10)

        self.edit.rok=Label(self.edit,text='rok',fg='white',bg='#8942D6')
        self.edit.rok.grid(row=2,column=0,sticky=W+E+N+S,ipadx=30,ipady=10)

        self.edit.reziser=Label(self.edit,text='reziser',fg='white',bg='#9E69D6')
        self.edit.reziser.grid(row=3,column=0,sticky=W+E+N+S,ipadx=40,ipady=10)

        self.edit.hodnotenie=Label(self.edit,text='hodnotenie',fg='white',bg='#9E69D6')
        self.edit.hodnotenie.grid(row=4,column=0,sticky=W+E+N+S,ipadx=40,ipady=10)
        
        self.edit.obsah=Label(self.edit,text='obsah',fg='white',bg='Medium Purple')
        self.edit.obsah.grid(row=5,column=0,columnspan=2, sticky=W+E+N+S,ipady=5)
            
        self.edit.naz=Entry(self.edit)
        self.edit.naz.grid(row=0,column=1,ipadx=30,ipady=10)

        self.edit.her=Entry(self.edit)
        self.edit.her.grid(row=1,column=1,ipadx=30,ipady=10)

        self.edit.R=Entry(self.edit)
        self.edit.R.grid(row=2,column=1,ipadx=30,ipady=10)

        self.edit.rez=Entry(self.edit)
        self.edit.rez.grid(row=3,column=1,ipadx=30,ipady=10)

        self.edit.hodnotenie=Entry(self.edit)
        self.edit.hodnotenie.grid(row=4,column=1,ipadx=30,ipady=10)

        
        self.edit.ob=Entry(self.edit)
        self.edit.ob.grid(row=5,column=0,columnspan=2,sticky=W+E+N+S,ipadx=50,ipady=10)
        if filmIx is not None:
            filmInfo = self.tab.main[filmIx]
            self.edit.naz.insert(0, filmInfo[0])
            self.edit.her.insert(0, filmInfo[1])
            self.edit.R.insert(0, filmInfo[2])
            self.edit.rez.insert(0, filmInfo[3])
            self.edit.ob.insert(0, filmInfo[4])
            self.edit.hodnotenie.insert(0, filmInfo[5])
        self.edit.uloz=Button(self.edit,text='uloz',bg='Sky Blue',command=(lambda:self.updateF(filmIx, edit)))
        self.edit.uloz.grid(row=6,column=1,ipadx=30,ipady=30,sticky=E)
        self.edit.mainloop()

    def updateF(self, filmIx, edit = False):
        if edit:
            self.zmaz(filmIx)
        self.pridajF()
    def pridajF(self):
        Film=[self.edit.naz.get(),self.edit.her.get(),self.edit.R.get(),self.edit.rez.get(),self.edit.ob.get(),self.edit.hodnotenie.get()]
        if not self.kontrolaVstupu(Film):
            return
        Tabulka.pridajFilm(self.tab,Film)
        self.tree.insert('','end',values=(Film[0],Film[1],Film[2],Film[3],Film[4],Film[5]),text=len(self.tab.main)-1)        
        self.edit.destroy()

    def kontrolaVstupu(self, Film):
        for stlpec in Film:
            if stlpec == '':
                return False
        try:
            int(Film[2])            
            if int(Film[5])>5 or int(Film[5])<0:
                self.OtvorUpozornenie()
                return False
        except ValueError:
            self.OtvorUpozornenie()
            return False
        return True
    def OtvorUpozornenie(self):
        self.Pozor=Tk()
        self.Pozor.title('CHYBA')
        self.Pozor['bg']='#9E69D6'
        Label(self.Pozor,text='Zadany rok alebo hodnotenie je neplatne,zvolte prosm inu hodnotu' ,bg='salmon',fg='white',padx=30,pady=30).pack()
        Button(self.Pozor,text='OK',font=('Helvetica',20),bg='#5A0DAC',command=(lambda:self.zavriUpozornenie()),fg='white',width=20).pack()        
    def zavriUpozornenie(self):
        self.Pozor.destroy()   
    def otvoredituprav(self):
        edit = Tk()
        edit.title('editacia')
        app2 = Frame2(master=root2)
        edit.mainloop()
        
    def uloz(self,t):
        s = ""
        print(self.tab.main)
        
        if len(self.tab.main)!=0:
            for pole in self.tab.main:
                for prvok in pole:
                    s+= prvok
                    if prvok != pole[len(pole)-1]:
                        s+="#"
                if pole != self.tab.main[len(self.tab.main)-1]:
                    s+="\n"

        subor=open(t, "w")
        subor.write(s)
        subor.close()

##_________________________________________________________

    
root = Tk()
root['bg']='black'
root.title('KINO FMFI')
app = uvitacieOkno(root)
root.mainloop()

