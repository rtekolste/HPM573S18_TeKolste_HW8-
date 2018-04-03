import Hw8Classes as Cls
import HW8Support as Support

#PROBLEM ONE

oldtrial = Cls.SetOfGames(id=1, prob_head=.5, n_games=1000)
newtrial = Cls.SetOfGames(id=2, prob_head=0.45, n_games=1000)
newsimulation = newtrial.simulation()
oldsimulation = oldtrial.simulation()
newearnings = newsimulation.get_ave_reward()*-1
oldearnings = oldsimulation.get_ave_reward()*-1

print("Problem 1")
print("On average the casino owner earns:", newearnings, "in steady state")
print("The difference with the weighted coin is:", newearnings - oldearnings, "in steady state")
print("With the weighted coin, the casino owner earns", 100*(oldearnings - newearnings)/oldearnings,
      "% less than with a fair coin in steady state")

#PROBLEM TWO
fair = Cls.MultipleGameSets(ids=range(100), prob_head=.5, n_games_in_a_set=100)
weighted = Cls.MultipleGameSets(ids=range(100), prob_head=.4, n_games_in_a_set=100)

fairsim = fair.simulation()
weightedsim = weighted.simulation()

print("Problem 2")
Support.print_outcomes(fair, "The coin is fair.")
Support.print_outcomes(weighted, "The coin is weighted.")
Support.print_comparative_outcomes(fair, weighted)
