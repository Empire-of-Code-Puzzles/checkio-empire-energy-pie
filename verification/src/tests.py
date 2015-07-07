TESTS = {
    "Basics": [
        {
            "input": [2, -1, 3],
            "answer": [1, 18],
            "show": "(2, -1, 3)",
            "explanation": [[1, 1], [2, 3], [5, 9], [1, 18]]
        },
        {
            "input": [1, 2, 3],
            "answer": [0, 1],
            "show": "(1, 2, 3)",
            "explanation": [[1, 1], [5, 6], [1, 2], [0, 1]]
        },
        {
            "input": [-1, -1, -1],
            "answer": [8, 27],
            "show": "(-1, -1, -1)",
            "explanation": [[1, 1], [2, 3], [4, 9], [8, 27]]
        },
        {
            "input": [10],
            "answer": [0, 1],
            "show": "(10,)",
            "explanation": [[1, 1], [0, 1]]
        },
        {
            "input": [99, -99],
            "answer": [1, 4],
            "show": "(99, -99)",
            "explanation": [[1, 1], [1, 2], [1, 4]]
        },
        {
            "input": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      -1],
            "answer": [99, 10000],
            "show": "[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]",
            "explanation": [[1, 1], [99, 100], [49, 50], [97, 100], [24, 25], [19, 20], [47, 50], [93, 100], [23, 25],
                            [91, 100], [9, 10], [89, 100], [22, 25], [87, 100], [43, 50], [17, 20], [21, 25], [83, 100],
                            [41, 50], [81, 100], [4, 5], [79, 100], [39, 50], [77, 100], [19, 25], [3, 4], [37, 50],
                            [73, 100], [18, 25], [71, 100], [7, 10], [69, 100], [17, 25], [67, 100], [33, 50], [13, 20],
                            [16, 25], [63, 100], [31, 50], [61, 100], [3, 5], [59, 100], [29, 50], [57, 100], [14, 25],
                            [11, 20], [27, 50], [53, 100], [13, 25], [51, 100], [1, 2], [49, 100], [12, 25], [47, 100],
                            [23, 50], [9, 20], [11, 25], [43, 100], [21, 50], [41, 100], [2, 5], [39, 100], [19, 50],
                            [37, 100], [9, 25], [7, 20], [17, 50], [33, 100], [8, 25], [31, 100], [3, 10], [29, 100],
                            [7, 25], [27, 100], [13, 50], [1, 4], [6, 25], [23, 100], [11, 50], [21, 100], [1, 5],
                            [19, 100], [9, 50], [17, 100], [4, 25], [3, 20], [7, 50], [13, 100], [3, 25], [11, 100],
                            [1, 10], [9, 100], [2, 25], [7, 100], [3, 50], [1, 20], [1, 25], [3, 100], [1, 50],
                            [1, 100], [99, 10000]]
        },
        {
            "input": [6, -4, 6, 24, 23, 65],
            "answer": [3, 2048],
            "show": "[6, -4, 6, 24, 23, 65]",
            "explanation": [[1, 1], [61, 64], [1891, 2048], [1795, 2048], [1411, 2048], [1043, 2048], [3, 2048]]
        },
        {
            "input": [83, 81],
            "answer": [0, 1],
            "show": "[83, 81]",
            "explanation": [[1, 1], [81, 164], [0, 1]]
        },
        {
            "input": [15, 33, 37, 16, -1, 22, -73, 66, -59, 10, -39, 57],
            "answer": [2682139399739, 14362129722368],
            "show": "[15, 33, 37, 16, -1, 22, -73, 66, -59, 10, -39, 57]",
            "explanation": [[1, 1], [413, 428], [95, 107], [343, 428], [327, 428], [139629, 183184], [130213, 183184],
                            [46225615, 78402752], [34135471, 78402752], [12595988799, 33556377856],
                            [11811961279, 33556377856], [4594852937531, 14362129722368],
                            [2682139399739, 14362129722368]]
        },
        {
            "input": [-86, 94, 3, 22, 30, -63, 72, 64, -52, -98, 93, -42, 52, -35, -52, 58, -5, 90, 70, 76],
            "answer": [2418384304303700202212, 19001162276662055889529],
            "show_answer": "[2418384304303700202212, 19001162276662055889529]",
            "show": "[-86, 94, 3, 22, 30, -63, 72, 64, -52, -98, 93, -42, 52, -35, -52, 58, -5, 90, 70, 76]",
            "explanation": [[1, 1], [1071, 1157], [977, 1157], [974, 1157], [952, 1157], [922, 1157],
                            [1008668, 1338649], [925364, 1338649], [851316, 1338649], [72361860, 119139761],
                            [76631209740, 137844703477], [65551211967, 137844703477], [73089601343205, 159486321922889],
                            [65921676762401, 159486321922889], [73964121327413922, 184525674464782573],
                            [6286950312830183370, 16422785027365648997], [5463681919064230352, 16422785027365648997],
                            [6294161570761993365504, 19001162276662055889529],
                            [4816110918299084955774, 19001162276662055889529],
                            [3666515966383489525984, 19001162276662055889529],
                            [2418384304303700202212, 19001162276662055889529]]
        },
        {
            "input": [-2, -19, -85, -73, -80, -88, 70, -66, 71, 17, -53, 9, -87, -94, 33, 64, 91, 95, 94, -52],
            "answer": [14944169998518287933224442117487, 90447599430824330991026825693467],
            "show_answer": "[14944169998518287933224442117487, 90447599430824330991026825693467]",
            "show": "[-2, -19, -85, -73, -80, -88, 70, -66, 71, 17, -53, 9, -87, -94, 33, 64, 91, 95, 94, -52]",
            "explanation": [[1, 1], [1241, 1243], [1518984, 1545049], [1758983472, 1920495907],
                            [2058010662240, 2387176412401], [2393466400185120, 2967260280614443],
                            [251313972019437600, 335300411709432059], [232431406597345690, 335300411709432059],
                            [24870160505915988830, 37888946523165822667], [22705948757609654631, 37888946523165822667],
                            [22187757212240532358, 37888946523165822667],
                            [26403431082566233506020, 47095960528295117575081],
                            [26062430563857741102017, 47095960528295117575081],
                            [30128169731819548713931652, 58540278936670831145825683],
                            [34617267021860661472307468148, 72765566718281843114261323969],
                            [32685437816950524044495220609, 72765566718281843114261323969],
                            [28938859965003590851162376897, 72765566718281843114261323969],
                            [23611694581766545216892239744, 72765566718281843114261323969],
                            [18050368082782816258038799859, 72765566718281843114261323969],
                            [12547581862735758130331185657, 72765566718281843114261323969],
                            [14944169998518287933224442117487, 90447599430824330991026825693467]]
        },
    ]
}
