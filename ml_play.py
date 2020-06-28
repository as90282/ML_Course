class MLPlay:
    def __init__(self, player):
        self.player = player
        if self.player == "player1":
            self.player_no = 0
        elif self.player == "player2":
            self.player_no = 1
        elif self.player == "player3":
            self.player_no = 2
        elif self.player == "player4":
            self.player_no = 3
        self.car_vel = 0
        self.car_pos = ()
        pass

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        self.car_pos = scene_info[self.player]
        if scene_info["status"] != "ALIVE":
            return "RESET"
        a=0
        b=0
        c=0
        d=-130
        dri_way=[35,105,175,245,315,385,455,525,595]
        f=[d,d,d,d,d,d,d,d,d]
        for car in scene_info["cars_info"]:       
            if car["id"]==self.player_no:
                self.car_vel = car["velocity"]
                self.car_pos = car["pos"]
                self.no = self.player_no
                
                for car in scene_info["cars_info"]:
                    for i in range(len(f)):
                        g = 35+70*(i-1)
                        if car["pos"][0] == g and car["pos"][1]<self.car_pos[1]+80 and car["id"]!=self.no:
                            if f[i-1]==d:
                                f[i-1]=car["pos"][1]
                            else:
                                if car["pos"][1]>f[i-1]:
                                    f[i-1]=car["pos"][1]      
        print(f)
        for car in scene_info["cars_info"]:
            if car["id"]==self.player_no :
                self.car_vel = car["velocity"]
                self.car_pos = car["pos"]
                if self.car_pos[0]>60 and self.car_pos[0]<105 :
                    if f[0]<f[1] and f[0]<f[2] and f[1]<f[2] :
                        return ["SPEED","MOVE_LEFT"]
                    elif f[0]<f[1] and f[0]>f[2] and f[1]>f[2] :
                        if f[1]<0:
                            return ["SPEED","MOVE_RIGHT"]
                        else :
                            return ["SPEED","MOVE_LEFT"]
                    else :
                        return ["SPEED","MOVE_RIGHT"]
                elif  self.car_pos[0]>=105 and self.car_pos[0]<=175 :
                    if f[1]<f[2] and f[1]<f[3] and f[2]<f[3] :
                        return ["SPEED","MOVE_LEFT"]
                    elif f[1]<f[2] and f[1]>f[3] and f[2]>f[3] :
                        if f[2]<0:
                            return ["SPEED","MOVE_RIGHT"]
                        else :
                            return ["SPEED","MOVE_LEFT"]
                    else :
                        return ["SPEED","MOVE_RIGHT"]
                elif  self.car_pos[0]>=175 and self.car_pos[0]<=245 :
                    if f[2]>f[3] :
                        return ["SPEED","MOVE_RIGHT"]
                    elif f[2]<f[3] :
                        return ["SPEED","MOVE_LEFT"]
                    else :
                        return ["SPEED"]
                elif  self.car_pos[0]>=245 and self.car_pos[0]<=315 :
                    if f[3]>f[4] :
                        return ["SPEED","MOVE_RIGHT"]
                    elif f[3]<f[4] :
                        return ["SPEED","MOVE_LEFT"]
                    else :
                        return ["SPEED"]
                elif  self.car_pos[0]>=315 and self.car_pos[0]<=385 :
                    if f[4]>f[5] :
                        return ["SPEED","MOVE_RIGHT"]
                    elif f[4]<f[5] :
                        return ["SPEED","MOVE_LEFT"]
                    else :
                        return ["SPEED"]
                elif  self.car_pos[0]>=385 and self.car_pos[0]<=455 :
                    if f[5]>f[6] :
                        return ["SPEED","MOVE_RIGHT"]
                    elif f[5]<f[6]  :
                        return ["SPEED","MOVE_LEFT"]
                    else :
                        return ["SPEED"]
                elif  self.car_pos[0]>=455 and self.car_pos[0]<=525 :
                    if f[6]>f[7] and f[5]>f[6] :
                        return ["SPEED","MOVE_RIGHT"]
                    elif f[6]>f[7] and f[6]>f[5] and f[7]>f[5] :
                        if f[6]<0:
                            return ["SPEED","MOVE_LEFT"]
                        else :
                            return ["SPEED","MOVE_RIGHT"]
                    else :
                        return ["SPEED","MOVE_LEFT"]
                elif  self.car_pos[0]>=455 and self.car_pos[0]<=525 :
                    if f[7]>f[8] and f[6]>f[7] and f[8]<f[6] :
                        return ["SPEED","MOVE_RIGHT"]
                    elif f[7]>f[8] and f[7]>f[6] and f[8]>f[6] :
                        if f[7]<0:
                            return ["SPEED","MOVE_LEFT"]
                        else :
                            return ["SPEED","MOVE_RIGHT"]
                    else :
                        return ["SPEED","MOVE_LEFT"]
                else :
                    return "SPEED"
        print(f)
        


    def reset(self):
        """
        Reset the status
        """
        pass


