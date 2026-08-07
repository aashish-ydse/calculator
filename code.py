import normal
import trigonometric
import logarithm
import geometry
option = input("what are you want? (option - normal calculator , trigonometric calculator,logarithm calculator,geometry calculator):")
if option == "normal calculator":
    normal.run()
elif option == "trigonometric calculator":
    trigonometric.run()
elif option == "logarithm calculator":
    logarithm.run()
elif option == "geometry calculator":
    geometry.run()
else:
    print("Invalid option")
 