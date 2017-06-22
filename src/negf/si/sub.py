from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Si",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=10000000
			,runner="negf"
		)
		app=dict(fmax=20.0,latx=4,laty=2,latz=1,supercell=[1,1,1])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
