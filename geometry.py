def run():
    pi=3.14159
    dimension=input("enter your shape dimension (option - 2D and 3D) :")
    if dimension=="2D":
        calculation_type=input("what do you want to calculate (option - area or perimeter):")
        if calculation_type=="area":
            shape=input("enter your shape name (option - 1.Square ,2.Rectangle , 3.Circle, 4.Triangle, 5.Parallelogram, 6.Rhombus, 7.Kite, 8.Trapezium, 9.Ellipse, 10.Semicircle, 11.Sector, 12.Annulus) :" )
            if shape=="square":
                side=float(input("enter length of side :"))
                area_square=side**2
                print(area_square)
            elif shape=="rectangle":
                side_len=float(input("enter length of rectangle :"))
                side_wid=float(input("enter width of rectangle :"))
                area_rectangle=side_len*side_wid
                print(area_rectangle)
            elif shape=="circle":
                cir_radius=float(input("enter radius of circle:"))
                radius_square=cir_radius**2
                area_circle=pi*radius_square
                print(area_circle)
            elif shape=="triangle":
                len_tri=float(input("enter length of triangle :"))
                base_tri=float(input("enter base of triangle :"))
                multi_len_base=len_tri*base_tri
                area_triangle=multi_len_base/2
                print(area_triangle)
            elif shape=="Parallelogram":
                len_par=float(input("enter length of Parallelogram :"))
                base_par=float(input("enter base of Parallelogram :"))
                area_Parallelogram=len_par*base_par
                print(area_Parallelogram)
            elif shape=="Rhombus":
                diagonal1=float(input("enter 1st diagonal :"))
                diagonal2=float(input("enter 2nd diagonal :"))
                multi_d1d2=diagonal1*diagonal2
                area_Rhombus=multi_d1d2/2
                print(area_Rhombus)
            elif shape=="Kite":
                diagonal1=float(input("enter 1st diagonal :"))
                diagonal2=float(input("enter 2nd diagonal :"))
                multi_d1d2=diagonal1 * diagonal2
                area_kite=multi_d1d2/2
                print(area_kite)
            elif shape=="Trapezium":
                side=float(input("enter side of Trapezium:"))
                base_tra=float(input("enter base of Trapezium:"))
                hight_tra=float(input("enter hight of Trapezium:"))
                sum_side_base=side + base_tra
                half_hight=hight_tra/2
                area_Trapezium=sum_side_base*half_hight 
                print(area_Trapezium)
            elif shape=="Semicircle":
                cir_radius=float(input("enter radius of circle:"))
                radius_square=cir_radius**2
                area_semicircle=(pi * radius_square)/2
                print(area_semicircle)
            elif shape=="Sector":
                cir_radius=float(input("enter radius of circle:"))
                angle=float(input("enter angle of sector :"))
                radius_square=cir_radius**2
                multi_pai_rad=(pi * radius_square)
                angle_div=angle/360
                area_sector=multi_pai_rad * angle_div
                print(area_sector)
            elif shape=="annulus":
                r1=float(input("enter inner radius :"))
                r2=float(input("enter outer radius :"))
                r1_square=r1**2
                r2_square=r2**2
                r2_r1=r2_square-r1_square
                area_annulus=pi*r2_r1
                print(area_annulus)
            elif shape=="polygon":
                side=float(input("enter numbers of sides of polygon :"))
                length=float(input("enter length of side :"))
                import math 
                tan=math.tan(math.pi/side)
                area_polygon=(side*(length**2))/(4*tan)
                print(area_polygon)
            else:
                print("sorry , i'm not capable for this calculation!")
        elif calculation_type=="perimeter":
            shape=input("enter your shape name (option - 1.Square ,2.Rectangle , 3.Circle, 4.Triangle, 5.Parallelogram, 6.Rhombus, 7.Kite, 8.Trapezium, 9.Ellipse, 10.Semicircle, 11.Sector, 12.Annulus :" )
            if shape=="square":
                side=float(input("enter length of side :"))
                perimeter_square=side*4
                print(perimeter_square)
            elif shape=="rectangle":
                side_len=float(input("enter length of rectangle :"))
                side_wid=float(input("enter width of rectangle :"))
                perimeter_rectangle=(side_len + side_wid)*2
                print(perimeter_rectangle)
            elif shape=="circle":
                cir_radius=float(input("enter radius of circle:"))
                pai=3.1415
                radius_2=cir_radius*2
                perimeter_circle=pai*radius_2
                print(perimeter_circle)
            elif shape=="triangle":
                len_tri_side1=float(input("enter length of side 1 :"))
                len_tri_side2=float(input("enter length of side 2 :"))
                base_tri=float(input("enter base of triangle :"))
                perimeter_triangle=len_tri_side1+len_tri_side2+base_tri
                print(perimeter_triangle)
            elif shape=="Parallelogram":
                len_par=float(input("enter length of side :"))
                base_par=float(input("enter base of Parallelogram :"))
                perimeter_Parallelogram=(len_par + base_par)*2
                print(perimeter_Parallelogram)
            elif shape=="Rhombus":
                side=float(input("enter length of side :"))
                perimeter_Rhombus=side*4
                print(perimeter_Rhombus)
            elif shape=="Kite":
                side1=float(input("enter length of side 1st :"))
                side2=float(input("enter length of side 2nd :"))
                perimeter_kite=(side1 + side2)*2
                print(perimeter_kite)
            elif shape=="Trapezium":
                side1=float(input("enter length of side 1st :"))
                side2=float(input("enter length of side 2nd :"))
                side3=float(input("enter length of side 3ed :"))
                side4=float(input("enter length of side 4th :"))
                perimeter_Trapezium=side1+side2+side3+side4
                print(perimeter_Trapezium)
            elif shape=="Semicircle":
                cir_radius=float(input("enter radius of circle:"))
                pai=3.1415
                radius_2=cir_radius*2
                perimeter_semicircle=(pai*cir_radius)+radius_2
                print(perimeter_semicircle)
            elif shape=="Sector":
                cir_radius=float(input("enter radius of circle:"))
                angle = float(input("enter angle of sector :"))
                pai = 3.1415
                radius_2 = cir_radius*2
                multi_pai_rad=(pai*radius_2)
                angle_div=angle/360
                perimeter_sector=(multi_pai_rad * angle_div)+radius_2
                print(perimeter_sector)
            elif shape=="annulus":
                r1=float(input("enter inner radius :"))
                r2=float(input("enter outer radius :"))
                r2_r1=r2 + r1 
                pai=3.1415
                pai2=pai*2
                perimeter_annulus=pai2*r2_r1
                print(perimeter_annulus)
            elif shape=="polygon":
                side=float(input("enter numbers of sides of polygon :"))
                length=float(input("enter length of side :"))
                perimeter_polygon=side*length
                print(perimeter_polygon)
            else:
                print("sorry , i'm not capable for this calculation!")
    elif dimension == "3D":
        calculation_type = input("what do you want to calculate (option -> surface area or volume :")
        if calculation_type == "surface area":
            shape = input("enter your shape name (option -> cube , cylinder , sphere , cone) :")
            if shape == "cube":
                side = float(input("enter length of side :"))
                area_cube = (side**2)*6
                print(area_cube)
            elif shape == "cylinder":
                rad_cy = float(input("enter radius of cylinder :"))
                height_cy = float(input("enter height of cylinder :"))
                rad_add_height = rad_cy + height_cy
                cir_peri = (pi*rad_cy)*2
                area_cylinder = cir_peri*rad_add_height
                print(area_cylinder)
            elif shape == "sphere":
                radius_sphere = float(input("enter radius of sphere :"))
                radius_2 = radius_sphere **2
                area_sphere = pi*radius_2*4
                print(area_sphere)
            elif shape == "cone":
                radius_cone = float(input("enter radius of cone :"))
                slant_height = float(input("enter slant height :"))
                area_cone = pi*radius_cone*(slant_height + radius_cone)
                print(area_cone)
            else:
                print("sorry , i'm not capable for this calculation!")
        elif calculation_type == "volume":
            shape = input("enter your shape name (option -> cube , cylinder , sphere , cone) :")
            if shape == "cube":
                side = float(input("enter length of side :"))
                volume_cube = side**3
                print(volume_cube)
            elif shape == "cylinder":
                rad_cy = float(input("enter radius of cylinder :"))
                height_cy = float(input("enter height of cylinder :"))
                volume_cylinder = pi*(rad_cy**2)*height_cy
                print(volume_cylinder)
            elif shape == "sphere":
                radius_sphere = float(input("enter radius of sphere :"))
                radius_3 = radius_sphere **3
                volume_sphere = (pi*radius_3*4)/3
                print(volume_sphere)
            elif shape == "cone":
                radius_cone = float(input("enter radius of cone :"))
                cone_height = float(input("enter cone height :"))
                volume_cone = (pi*(radius_cone**2)*cone_height)/3
                print(volume_cone)
            else:
                print("sorry , i'm not capable for this calculation!")



