#largest ever measured is in chile 9.5 in 1960
#prompt a user to enter a Rc measuremenet,accept floating point value and do some calculations and display the equivalent amount of energy in joules and in tons of exploded TNT for that user-selected value.

#The Richter scale is a way to quantify the magnitude of an earthquake using a base-10 logarithmic scale.The magnitude is defined as the logarithm of the ratio of the amplitude of  waves measured by a seismograph to an arbitrary small amplitude.

#An earthquake that measures 5.0 on the Richter scale has a shaking amplitude 10 times larger than one that measures 4.0, and corresponds to a 31.6 times larger release of energy.

# the energy in joules released for a particualr richter scale measurement is given by:
    # Energy = 10**(1.5*rc_measure) + 4.8
#one ton of exploded TNT yields 4.184*10**9 joules.

#ok enough of this chitchat
rc_input = input("enter a number sir/madam?")
rc_input_float = float(rc_input)
energy = 10**(1.5*rc_input_float) + 4.8
tons_of_tnt = energy / 4.184*10**9

print "energy :" + str(energy)
print "tons of TNT:" + str(tons_of_tnt)
