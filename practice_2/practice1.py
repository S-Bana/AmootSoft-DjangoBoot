# Theater seat reservation system

reservation_list = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]

def reserv(x= 0,y=0,reservation_list=[]):
    reserv = reservation_list[x][y]
    if reserv == 0 :
        reservation_list[x][y] = 1
        return 'The desired seat has been reserved for you'
    else:
        return 'please choice another seat.' 

def check_input(x):
    if x >0 and x < 6 :
        return False
    return True


while True:
    command = input('Do you want to reserve a seat? : (y or n)')
    if command== 'n':
        break
    row,column = -1,-1
    while check_input(row):
        
        try:
            row = int(input('select row : ')) -1
        except Exception as e:
            print (e)
    while check_input(column):
        try:
            column = int(input('select column : ')) -1
        except Exception as e:
            print (e)

    print(reserv(x = row, y= column, reservation_list=reservation_list))