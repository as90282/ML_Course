"""
The template of the script for the machine learning process in game pingpong
"""

# Import the necessary modules and classes
from games.pingpong.game import gamecore
from mlgame.communication import ml as comm

def ml_loop(side: str):
    """
    The main loop for the machine learning process
    The `side` parameter can be used for switch the code for either of both sides,
    so you can write the code for both sides in the same script. Such as:
    ```python
    if side == "1P":
        ml_loop_for_1P()
    else:
        ml_loop_for_2P()
    ```
    @param side The side which this script is executed for. Either "1P" or "2P".
    """
    
    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here
    scene = gamecore.Scene("HARD")
    ball_served = False
    def move_to(player, pred) : #move platform to predicted position to catch ball 
        if player == '1P':
            if scene_info["platform_1P"][0]+20  > (pred-10) and scene_info["platform_1P"][0]+20 < (pred+10): return 0 # NONE
            elif scene_info["platform_1P"][0]+20 <= (pred-10) : return 1 # goes right
            else : return 2 # goes left
        else :
            if scene_info[" platform_2P"][0]+20  > (pred-10) and scene_info["platform_2P"][0]+20 < (pred+10): return 0 # NONE
            elif scene_info["platform_2P"][0]+20 <= (pred-10) : return 1 # goes right
            else : return 2 # goes left


    def ml_loop_for_1P():
        speed = [7 + (scene_info["frame"]//200),7 + (scene_info["frame"]//200)]
        if scene_info["ball_speed"][0] > speed[0]  :
            speed[0] = scene_info["ball_speed"][0]
        elif scene_info["ball_speed"][0] < -speed[0] :
            speed[0] = -scene_info["ball_speed"][0]
        if scene_info["ball"][1] == 80  : # 球正在向下 # ball goes down
            h1 = (155//speed[1])
            h = (175 // speed[1])
            b_x = scene_info["blocker"][0]+ scene._blocker._speed[0]*(h+1)
            if b_x > 170 :
                b_x = 170 - 30*((b_x - 170)//30)
            elif b_x < 0 :
                b_x = 30*((0 - b_x)//30)
            if scene_info["ball_speed"][0] > 0 :
                y1 = (195-scene_info["ball"][0]) // speed[0]
                y1_pred = 80 + speed[1]*(y1+1)
                if y1_pred < 260 :
                    y_b = 80 + speed[1]*h1
                    h_x1 = 195 - speed[1]*(h1-y1-1)
                    h_x2 = 195 - speed[1]*(h-y1-1)
                    if (235-y_b<= h_x1-(b_x+30) and 260-y_b >= h_x1-(b_x+30)) or (h_x2>b_x+30 and h_x2< b_x+30+speed[0]+scene._blocker._speed[0]):
                        y3_pred = y_b + (195-(b_x+30))
                        if 415-y3_pred > 195 :
                            y4 = 195 // speed[1]
                            y4_pred = y3_pred + speed[1]*(y4+1)
                            x_pred = 415 - y4_pred
                            print(1)
                        else :
                            x_pred = 195- (415- y3_pred)
                            print(2)
                        return x_pred
                    elif 415-y1_pred > 195 :
                        y2 = 195 // speed[1]
                        y2_pred = y1_pred + speed[1]*(y2+1)
                        x_pred = 415 - y2_pred
                        print(3)
                    else :
                        x_pred = 195- (415- y1_pred)
                        print(4)
                    return x_pred
                elif 415- y1_pred > 195 :
                    y2 = 195 // speed[1]
                    y2_pred = y1_pred + speed[1]*(y2+1)
                    x_pred = 415 - y2_pred
                    print(7)
                else :
                    x_pred = 195- (415- y1_pred)
                    print(8)
                return x_pred
            elif scene_info["ball_speed"][0] < 0 :
                y1 = (scene_info["ball"][0]) // speed[0]
                y1_pred = scene_info["ball"][1] + speed[1]*(y1+1)
                if y1_pred < 260 :
                    y_b = 80 + speed[1]*h
                    h_x1 = speed[1]*(h-y1-1)
                    if 235-y_b<= b_x-h_x1 and 260-y_b >= b_x-h_x1:
                        y3_pred = y_b + b_x
                        if 415-y3_pred > 195 :
                            y4 = 195 // speed[1]
                            y4_pred = y3_pred + speed[1]*(y4+1)
                            x_pred = 195-(415 - y4_pred)
                            print(1)
                        else :
                            x_pred = (415- y3_pred)
                            print(2)
                        return x_pred
                    elif 415-y1_pred > 195 :
                        y2 = 195 // speed[1]
                        y2_pred = y1_pred + speed[1]*(y2+1)
                        x_pred = 195-(415 - y2_pred)
                    else :
                        x_pred = 415- y1_pred
                    return x_pred
                elif 415-y1_pred > 195 :
                    y2 = 195 // speed[1]
                    y2_pred = y1_pred + speed[1]*(y2+1)
                    x_pred = 195-(415 - y2_pred)
                else :
                    x_pred = 415- y1_pred
                return x_pred
            elif 415-y1_pred > 195 :
                y2 = 195 // speed[1]
                y2_pred = y1_pred + speed[1]*(y2+1)
                x_pred = 195-(415 - y2_pred)
            else :
                x_pred = 415- y1_pred
            return x_pred
        elif scene_info["ball"][1] == 415 :
            x1 = 155//speed[1]
            if scene_info["ball_speed"][0] > 0 :
                y1 = (195 - scene_info["ball"][0])//speed[0]
                y1_pred = 415 - speed[0]*(y1+1)
                if y1_pred <= 260 :
                    x1_pred = scene_info["ball"][0] + speed[0]*(x1+1)
                    y2 = (195 - x1_pred)//speed[0]
                    y2_pred = 260 + speed[1]*(y2+1)
                    x_pred = 195 - (415-y2_pred)
                else :
                    x2 = (y1_pred - 260)//speed[1]
                    x2_pred = 195 - speed[0]*(x2+1)
                    if x2_pred >= 155 :
                        x_pred = x2_pred -155
                    else :
                        y3 = x2_pred // speed[0]
                        y3_pred = 260 + speed[1]*(y3+1)
                        if y3_pred >=415:
                            x_pred = 0
                        else :
                            x_pred = 415-y3_pred
                        return x_pred
                    return x_pred
                return x_pred
            elif scene_info["ball_speed"][0] < 0 :
                y1 = (195 - scene_info["ball"][0])//speed[0]
                y1_pred = 415 - speed[0]*(y1+1)
                if y1_pred <= 260 :
                    x1_pred = scene_info["ball"][0] - speed[0]*(x1+1)
                    y2 =  x1_pred//speed[0]
                    y2_pred = 260 + speed[1]*(y2+1)
                    x_pred = (415-y2_pred)
                else :
                    x2 = (y1_pred - 260)//speed[1]
                    x2_pred = speed[0]*(x2+1)
                    if x2_pred <= 45 :
                        x_pred = x2_pred + 155
                    else :
                        y3 = (195-x2_pred) // speed[0]
                        y3_pred = 260 + speed[1]*(y3+1)
                        if y3_pred >=415:
                            x_pred = 200
                        else :
                            x_pred = 195-(415-y3_pred)
                        return x_pred
                    return x_pred
                return x_pred

        elif scene_info["ball_speed"][1] < 0 and scene_info["ball"][1] < 260 :
            x_pred = 100
            return x_pred
        elif (scene_info["blocker"][0] > 30 and scene_info["blocker"][0] < 60 and scene_info["ball"][1]<240 and scene_info["ball"][1]>180) or (scene_info["blocker"][0] > 140 and scene_info["blocker"][0] < 170 and scene_info["ball"][1]<240 and scene_info["ball"][1]>180) :
            x_pred = 100
            return x_pred
        elif scene_info["ball_speed"][1] > 0 and scene_info["ball"][1] > 240 : # 球正在向下 # ball goes down
            x = ( scene_info["platform_1P"][1]-scene_info["ball"][1] ) // scene_info["ball_speed"][1] # 幾個frame以後會需要接  # x means how many frames before catch the ball
            pred = scene_info["ball"][0]+(scene_info["ball_speed"][0]*x)  # 預測最終位置 # pred means predict ball landing site 
            bound = pred // 200 # Determine if it is beyond the boundary
            if (bound > 0): # pred > 200 # fix landing position
                if (bound%2 == 0) : 
                    pred = pred - bound*200                    
                else :
                    pred = 200 - (pred - 200*bound)
            elif (bound < 0) : # pred < 0
                if (bound%2 ==1) :
                    pred = abs(pred - (bound+1) *200)
                else :
                    pred = pred + (abs(bound)*200)
            return pred
        



    def ml_loop_for_2P():  # as same as 1P
        if scene_info["ball_speed"][1] > 0 : 
            return move_to(player = '2P',pred = 100)
        else : 
            x = ( scene_info["platform_2P"][1]+30-scene_info["ball"][1] ) // scene_info["ball_speed"][1] 
            pred = scene_info["ball"][0]+(scene_info["ball_speed"][0]*x) 
            bound = pred // 200 
            if (bound > 0):
                if (bound%2 == 0):
                    pred = pred - bound*200 
                else :
                    pred = 200 - (pred - 200*bound)
            elif (bound < 0) :
                if bound%2 ==1:
                    pred = abs(pred - (bound+1) *200)
                else :
                    pred = pred + (abs(bound)*200)
            return move_to(player = '2P',pred = pred)

    # 2. Inform the game process that ml process is ready
    comm.ml_ready()
    x = [1]
    # 3. Start an endless loop
    while True:
        # 3.1. Receive the scene information sent from the game process
        scene_info = comm.recv_from_game()

        # 3.2. If either of two sides wins the game, do the updating or
        #      resetting stuff and inform the game process when the ml process
        #      is ready.
        if scene_info["status"] != "GAME_ALIVE":
            # Do some updating or resetting stuff
            ball_served = False

            # 3.2.1 Inform the game process that
            #       the ml process is ready for the next round
            comm.ml_ready()
            continue

        # 3.3 Put the code here to handle the scene information

        # 3.4 Send the instruction for this frame to the game process
        
        if not ball_served:
            comm.send_to_game({"frame": scene_info["frame"], "command": "SERVE_TO_LEFT"})
            ball_served = True
        else:
            try :
                x_pred = ml_loop_for_1P()
                
                if scene_info["platform_1P"][0]+10 >= x_pred:
                    comm.send_to_game({"frame": scene_info["frame"], "command": "MOVE_LEFT"})
                elif scene_info["platform_1P"][0]+30 <= x_pred:
                    comm.send_to_game({"frame": scene_info["frame"], "command": "MOVE_RIGHT"})
                else :
                    comm.send_to_game({"frame": scene_info["frame"], "command": "NONE"})
            except TypeError :
                x_pred = x[-1]
                
                if scene_info["platform_1P"][0]+10 >= x_pred:
                    comm.send_to_game({"frame": scene_info["frame"], "command": "MOVE_LEFT"})
                elif scene_info["platform_1P"][0]+30 <= x_pred:
                    comm.send_to_game({"frame": scene_info["frame"], "command": "MOVE_RIGHT"})
                else :
                    comm.send_to_game({"frame": scene_info["frame"], "command": "NONE"})
            x.append(x_pred)