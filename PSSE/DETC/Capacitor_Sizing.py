# POI Voltage 1.04 Vpu
psspy.plant_chng_4(9, 0, [_i, _i], [1.04, _f])
# Max Lagging
ierr, iarray = psspy.amachint(-1, 4, 'NUMBER')
for i_bus in iarray[0]:
    #print(i_bus)
    if i_bus != 9:
        ierr, rval = psspy.macdat(i_bus, '1', 'QMAX')
        psspy.machine_chng_2(i_bus,r"""1""",[_i,_i,_i,_i,_i,_i],[_f,_f,_f, rval,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
ierr = psspy.fnsl([0, 0, 0, 1, 1, 1, 0, 0])
# Tap MPT DETC
psspy.two_winding_chng_6(1,8,r"""1""",[_i,_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, 1.025,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"",r"""YNYN0""")
psspy.two_winding_chng_6(2,8,r"""1""",[_i,_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, 1.025,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"",r"""YNYN0""")
psspy.two_winding_chng_6(3,8,r"""1""",[_i,_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, 1.025,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"",r"""YNYN0""")
s_output = "psspy.two_winding_chng_6(1,8,r\"1\",[_i,_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, 1.025,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],\"\",r\"YNYN0\")\n"
s_output += "psspy.two_winding_chng_6(2,8,r\"1\",[_i,_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, 1.025,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],\"\",r\"YNYN0\")\n"
s_output += "psspy.two_winding_chng_6(3,8,r\"1\",[_i,_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, 1.025,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],\"\",r\"YNYN0\")\n"
ierr = psspy.fnsl([0, 0, 0, 1, 1, 1, 0, 0])
# Tap WTT DETC
l_bus = [201005, 201006, 201007, 201008, 201009, 201010, 201042, 201043, 201082, 201083, 201084, 201085, 201086, 201087, 202015, 202016, 
202017, 202018, 202019, 202020, 202047, 202048, 202049, 202050, 202051, 202052, 202090, 202091, 202092, 202093, 202094, 202095, 203024,
203025, 203026, 203027, 203028, 203029, 203056, 203057, 203058, 203059, 203060, 203061, 203099, 203100, 203101, 203102, 203103, 203104, 
204033, 204034, 204035, 204036, 204037, 204038, 204063, 204064, 204065, 204066, 204067, 204068, 204106, 204107, 204108, 204109, 204110, 
204111, 204112, 204113, 204114, 204115, 204116, 205073, 205074, 205075, 205076, 205077, 205078]
f_max_v = 0.0
i_max_v_bus = 0
for i_bus in l_bus:
    ierr, rval = psspy.busdat(i_bus, 'PU')
    print("bus %i voltage %.3f\n" % (i_bus, rval))
    if rval > f_max_v:
        f_max_v = rval
        i_max_v_bus = i_bus
print("bus %i voltage %.3f\n" % (i_max_v_bus, f_max_v))
i_count = 0
while f_max_v > 1.1:
    f_max_v = 0.0
    i_max_v_bus = 0
    for i_bus in l_bus:
        ierr, rval = psspy.busdat(i_bus, 'PU')
        if rval > f_max_v:
            f_max_v = rval
            i_max_v_bus = i_bus
    if f_max_v > 1.125:
        f_ratio = 1.05
    else:
        f_ratio = 1.025
    psspy.two_winding_chng_6(i_max_v_bus, i_max_v_bus + 200000,r"""1""",[_i,_i,_i,_i,_i,_i,_i,_i,i_max_v_bus + 200000,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, f_ratio,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"",r"""DYN5""")
    s_output += "psspy.two_winding_chng_6(%i,%i,r\"1\",[_i,_i,_i,_i,_i,_i,_i,_i,%i,_i,_i,_i,1,_i,_i,_i],[_f,_f,_f,_f,_f,_f, %.3f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],\"\",r\"DYN5\")\n" % (i_max_v_bus, i_max_v_bus + 200000, i_max_v_bus + 200000, f_ratio)
    ierr = psspy.fnsl([0, 0, 0, 1, 1, 1, 0, 0])
    i_count += 1
    if i_count > 50:
        f_max_v = 0.0
with open(r"DETC.py", r"w") as f:
    f.write(s_output)
f_capacitor = 0.5
ierr, cmpval = psspy.brnflo(8, 9, '1')
while 0.329*cmpval.real < cmpval.imag + 0.5:
    ierr = psspy.shunt_chng(1, r"1", 1, [_f, f_capacitor])
    ierr = psspy.shunt_chng(2, r"1", 1, [_f, f_capacitor])
    ierr = psspy.shunt_chng(3, r"1", 1, [_f, f_capacitor])
    ierr = psspy.fnsl([0, 0, 0, 1, 1, 1, 0, 0])
    ierr, cmpval = psspy.brnflo(8, 9, '1')
    f_capacitor += 0.5