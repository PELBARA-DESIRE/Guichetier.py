class Guichetier:
	def __init__(self,id,nom,age,solde):
		self.id=id
		self.nom=nom
		self.age=age
		self.solde=solde
		print("le solde du client  ",nom," est : ",solde)
	def depot(self):
		sum=float(input("entrez le montant à verser :"))
		print("depot de : ",sum," sur le compte de : ",self.nom)
		self.solde=self.solde+sum
		print("nouveau solde : ",self.solde)		
	def retrait(self):
		sum=float(input("entrez le montant à retirer : "))
		if sum>self.solde:
			print("transaction impossible le solde de ",self.nom," est insuffisant")
		else:
			self.solde=self.solde-sum
			print("retrait de : ",sum," sur le compte de : ",self.nom)
			print("nouveau solde : ",self.solde)
	def modif(self):
		print("modification des données du client : ",self.nom)
		self.id=int(input("entrez le nouvel identifant du client : "))
		self.nom=input("entrez le nouveau nom du client : ")
		self.age=int(input("entrez le nouvel age du client : "))
		print("les nouvelles informations du client sont : \n identifiant :",self.id," \n nom: ",self.nom," \n age : ",self.age,"\n solde (non modifiable si ce n'est par une transaction ) : ",self.solde)
c= Guichetier(0,"Abdel",13,5000)
c.depot()
c.retrait()
print("le solde de ",c.nom," est de ",c.solde)