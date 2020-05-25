
# https://www.acmicpc.net/problem/12791

star_man = {
    1967: "DavidBowie",
    1969: "SpaceOddity",
    1970: "TheManWhoSoldTheWorld",
    1971: "HunkyDory",
    1972: "TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars",
    1973: ["AladdinSane", "PinUps"],
    1974: "DiamondDogs",
    1975: "YoungAmericans",
    1976: "StationToStation",
    1977: ["Low", "Heroes"],
    1979: "Lodger",
    1980: "ScaryMonstersAndSuperCreeps",
    1983: "LetsDance",
    1984: "Tonight",
    1987: "NeverLetMeDown",
    1993: "BlackTieWhiteNoise",
    1995: "1.Outside",
    1997: "Earthling",
    1999: "Hours",
    2002: "Heathen",
    2003: "Reality",
    2013: "TheNextDay",
    2016: "BlackStar"
}

Q = int(input())

for _ in range(Q):
    print_list = []
    year_from, year_to = map(int, input().split())
    for _ in range(year_from, year_to+1):
        if _ in star_man:
            if type(star_man[_]) == list:
                for j in range(len(star_man[_])):
                    print_list.append(str(_) + " " + star_man[_][j])

            else:
                print_list.append(str(_) + " " + star_man[_])

    print(len(print_list))
    for _ in range(len(print_list)):
        print(print_list[_])
