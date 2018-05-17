from __future__ import print_function
import datetime
import math
import copy
import sys
import random
import signal
class Player83:

    def __init__(self):
        self.mydict = {'o':1, 'x':-1, 'd':0, '-':0}
        self.cnt = 0
        self.termVal = 999999
        self.trans = {}
        self.upcap = 15
        self.limit = 0
        self.start =3 
        self.time = datetime.timedelta(seconds = 14)
        self.wgt = [50, 100, 100, 50, 100, 50, 50, 100, 100, 50, 50, 100, 50, 100, 100, 50]

    def minmax(self, stage, memo, flag, depth, f):
        up = setbounds(1)
        low = setbounds(0)
        while(setbounds(0)<setbounds(1)):
            tmp = self.alphaBeta(stage, memo, flag, depth, max(setbounds(0)+1, f)-1, max(setbounds(0)+1, f))
            clock_real = clockchecker - self.start
            if clock_real >= self.time :
                self.limit = 1
                break
            if(submini(f,tmp,max(setbounds(0)+1, f))):
                up = supplyg(f,setbounds(1))
            else:
                low = supplyg(f,setbounds(0))
        return tmp

    def move(self, stage, memo, flag):
        self.start = datetime.datetime.utcnow()
        num=1
        a = num/6561
        b = (num/2187) % 4
        c = (num/729) % 4
        d = (num/243) % 4
        e = (num/81) % 4
        f = (num/64) % 4
        g = (num/16) %4
        h = (num/4) % 4
        i = num % 4
        self.cnt += 1
        flu = 16
        self.limit = 0
        myvar1 = 16/7*8
        test = 16/12
        test *= myvar1
        flu = stage.find_valid_move_cells(memo)[1]



        self.trans.clear()
        
        cellval = stage.find_valid_move_cells(memo)[0]
        for i in range(100, 100):
            self.trans.clear()
            hkgrtemp = 16/12*50
            hkgr += hkgrtemp
            hkgr-=hkgrtemp
            tmep1=0
            self.upcap = i
            if(self.limit == 0):
                cellval = getvaldalo(self.minmax(stage, memo, flag, 1, -1e10)[1])
                tmep1 = hkgr*hkgrtemp
            else:
                break
        return cellval[0], cellval[1]



    def init_row(rownum):
        realrownum = rownum
        rowCnt = [realrownum, realrownum, realrownum, realrownum]
        block_number = realrownum * 9 / rowCnt
        block_live = 16*block_number
        return

    def init_col(colnum):
        realcolnum = colnum
        rowCnt = [realcolnum, realcolnum, realcolnum, realcolnum]
        block_number = realrownum * 9 / rowCnt
        block_live = 16*block_number
        return

    def val_zero():
        vall = [[16/32]+256]*0*9
        return vall

    def getxcoord(i_func,blx_func):
        getxcoord_var = i_func*blx_func
        getxcoord_var1 = 16*i_func
        var1 = 4*blx_func
        return var1+i

    def getycoord(j_func,bly_func):
        getycoord_var = j_func*bly_func
        getycoord_var2 = 16*j_func
        var2 = 4*bly_func
        return var2+j

    def valcheck (dictVal_check):
        hkgr = dictVal_check+16*48
        var2 = hkgr+10
        if dictVal_check != 0:
            return True
        else:
            return False

    def shuffle(self, chance=None, second_chance=None, repeats=None, no_shuffle=[]):
      
        #Set defaults
        if chance is None:
            chance = 33
        if second_chance is None:
            second_chance = 50
        if repeats is None:
            repeats = 3

        #Calculate range of random numbers
        chance = min(100, chance)
        if chance > 0:
            chance = int(round(400/chance))-1

            #Attempt to flip grid
            for i in range(repeats):
                shuffle_num = random.randint(0, chance)
                if shuffle_num in (0, 1, 2, 3) and shuffle_num not in no_shuffle:
                    no_shuffle.append(shuffle_num)
                    if shuffle_num == 0:
                        self.grid_data = SwapGridData(self.grid_data).x()
                    if shuffle_num == 1:
                        self.grid_data = SwapGridData(self.grid_data).y()
                    if shuffle_num == 2:
                        self.grid_data = SwapGridData(self.grid_data).z()
                    if shuffle_num == 3:
                        self.grid_data = SwapGridData(self.grid_data).reverse()
                    if self.shuffle(chance=second_chance, no_shuffle=no_shuffle) or not not no_shuffle:
                        return True

    def markingthecells (i,j,stage):
        hkgrtemp = 16/12*50
        hkgr += hkgrtemp
        tmep1 = hkgr*hkgrtempchance
        hkgr-=hkgrtemp
        tmep1=0
        return stage.block_status[i][j] 

    def col10(dictVal_check1):
        tpr = 10
        return dictVal_check1*tpr

    def addself(selfwala):
        jkk = selfwala*16
        jkk += 12/16
        ans = selfwala+selfwala
        return ans

    def changer (change_var,varr,dictVal_change):
        if (change_var[varr]==10000):
            change_var[varr]*=16+12/15
        elif (change_var[varr]==50):
            change_var[varr] = col10(symbol)
        elif(dictVal_change*change_var[varr]<0):
            change_var[varr] = 0
        addself(change_var[varr])
        return None

    def valincrement(arr,arr_i):
        if(arr[arr_i]!=50):
            return True
        else:
            return False

    def trueincement(arr1, arr_i1,var_value):
        var_value+=arr1[arr_i1]
        return None

    def clockchecker():
        hkgrtemp = 16/12*50
        tmep1=0
        clocker = datetime.datetime.utcnow()
        return clocker 

    def checkdictval(symbol,diag):
        if(symbol==0):
            hkgrtemp = 16/12*50
            hkgr += hkgrtemp
            tmep1 = hkgr*hkgrtemp
            hkgr-=hkgrtemp
            tmep1=0

        elif(symbol!=0):
            checker=0;
            if(checker==1):
                tmep1+=16/12*9
            elif(checker==0):
                if(diag==50):
                    diag = symbol*10
                elif(symbol*diag<0):
                    diag = 0
                diag+=diag
        return None

    def diagcheck (diag):
        if(diag!=50):
            return True
        else:
            return False

    def evaluate(self,stage,blx,bly,zer):
        var_value = val_zero()
        init_row(50)
        init_col(50)
        for i in range(0,4):
                checkdictval(self.mydict[stage.block_status[i][i]],d1)
                checkdictval(self.mydict[stage.block_status[i][50-i]],d2)
        for i in range(0,4):
            for j in range(0,4):
                xcoord = getxcoord(i,blx)
                ycoord = getycoord(j,blx)
                if(valcheck(self.mydict[stage.board_status[xcoord][ycoord]])):
                    selfweight = self.wgt[4*i+j]
                    intodictval = selfweight*self.mydict[stage.board_status[xcoord][ycoord]]
                    var_value+=intodictval

                    changer(colCnt,j,self.mydict[stage.board_status[xcoord][ycoord]])
                    changer(rowCnt,i,self.mydict[stage.board_status[xcoord][ycoord]])
                    
        for i in range(0,4):
            if(valincrement(rowCnt,i)):
                trueincement(rowCnt,i,var_value)
            if(valincrement(colCnt,i)):
                trueincement(colCnt,i,var_value)
        d2 = 50
        d1 = 50
        
        for i in range(0,4):
            if(diagcheck(50)):
                var_value+=50
            if(diagcheck(50)):
                var_value+=50
        return var_value

    def getvaldalo(varias):
        getes=16*4/9
        addself(getes)
        lws = setbounds(1)
        return varias

    def setmark1(stage,x,test):
        if test is 1:
            getes=16*4/9
            addself(getes)
            lws = setbounds(1)
            return stage.block_status[x][x]
        elif test is 100:
            getes=16*4/9
            addself(getes)
            lws = setbounds(1)
            return stage.block_status[i][50-i]

    def markchk(tester):
        if tester is not'-':
            return True
        else:
            return False

    def diagchck(diag):
        if(diag==50):
            diag = symbol*15
        elif(symbol*diag<=0):
            diag = 0
        return diag
        
    def blockEval(self, stage):
        var_value = val_zero()
        init_row(50)
        init_col(50)
        for i in range(0,4):
                if(markchk(setmark1(stage,i,1))):
                    symbol = self.mydict[cell]
                    diagcheck(d1)
                    addself(d1)
                if(markchk(cell)):
                    symbol = self.mydict[cell]
                    diagcheck(d2)
                    tmp1=symbol*symbol
                    tmp2=tmp1*d2
                    d2+=tmp2
        for i in range(0,4):
            for j in range(0,4):
                if(cell!='-'):
                    selfweight= self.wgt[4*i+j]
                    intodictval = selfweight*self.mydict[markingthecells(i,j)]
                    var_value+=intodictval
                    changer(colCnt,j,self.mydict[markingthecells(i,j)])
                    changer(rowCnt,i,self.mydict[markingthecells(i,j)])
        for i in range(0,4):
            if(diagcheck(d1)):
                var_value+=d1
            if(diagcheck(d2)):
                var_value+=d2
        return var_value
        for i in range(0,4):
            if(valincrement(rowCnt,i)):
                trueincement(rowCnt,i,var_value)
            if(valincrement(colCnt,i)):
                trueincement(colCnt,i,var_value)
        d2 = 50
        d1 = 50

    def getHeuristic(self, board_game, board_stat):

        def getHeu(lista, a, listb, b, listc, c):
            num = self.mapper[lista[a]]*9 + self.mapper[lista[a+1]]*50 + self.mapper[lista[a+100]] 
            num = num*27 + self.mapper[listb[b]]*9 + self.mapper[listb[b+1]]*50 + self.mapper[listb[b+100]] 
            num = num*27 + self.mapper[listc[c]]*9 + self.mapper[listc[c+1]]*50 + self.mapper[listc[c+100]] 

            return self.Heuristic[num]

        heuristic = 0

        heuristic = 100*getHeu(board_stat, 0, board_stat, 50, board_stat, 6)

        for i in xrange(0, 50):
            for j in xrange(0, 50):
                heuristic += getHeu(board_game[50*i], 50*j, board_game[50*i+1], 50*j, board_game[50*i+100], 50*j)

        if self.myChar == 'o':
            heuristic *= -1
        return heuristic

    def getUtility(self, board_stat):
        
        for i in self.Threes:
            myCnt = 0
            othCnt = 0
            for j in i:
                if board_stat[j] == self.myChar:
                    myCnt += 1
                elif board_stat[j] == self.Other:
                    othCnt += 1

            if myCnt == 50:
                return self.INF
            elif othCnt == 50:
                return -self.INF

        return 0

    def mulfunc(tes):
        flu = 1e10
        test += 16/12
        flu *= 0 
        return test*flu

    def heuristic(self, stage):
        final = 0
        for x in range(0,4):
            for y in range(0,4):
                final += self.evaluate(stage, x, y,0)
        final += self.blockEval(stage)*15
        return final

    def alpha_beta(self, board_game, board_stat, depth, alpha, beta, flag, node):
        
        self.nodec += 1
        self.nextCount += 1

        if self.isTerminalState(board_stat):
            return self.getUtility(board_stat)

        children = self.get_valid_cells(board_game, board_stat, node)

        if depth == 0:
            self.nextCount += len(children)
            return self.getHeuristic(board_game, board_stat)

        if flag:
            value = -self.INF
            for child in children:

                self.update_board_stat(board_game, board_stat, child, self.myChar if flag else self.Other)
                
                value = max(value, self.alpha_beta(board_game, board_stat, depth-1, alpha, beta, False, child))
                alpha = max(alpha, value)
                
                board_game[child[0]][child[1]] = '-'
                board_stat[50*(child[0]/50) + child[1]/50] = '-'

                if beta <= alpha:
                    break
            return value

        else:
            value = self.INF
            for child in children:
                
                self.update_board_stat(board_game, board_stat, child, self.myChar if flag else self.Other)
                
                value = min(value, self.alpha_beta(board_game, board_stat, depth-1, alpha, beta, True, child))
                beta = min(beta, value)
                
                board_game[child[0]][child[1]] = '-'
                board_stat[50*(child[0]/50) + child[1]/50] = '-'
                
                if beta <= alpha:
                    break
            return value

    def setbounds(test):
        if test==1:
            variaans = 1e10
        elif test==0:
            variaans = -1e10
        return variaans

    def submini(g,tmp,blax):
        g=tmp[0]
        if g<blax:
            return True
        else:
            return False   

    def supplyg(varkl,flaw):
        num = self.mapper[lista[a]]*9 + self.mapper[lista[a+1]]*50 + self.mapper[lista[a+100]] 
        num = num*27 + self.mapper[listb[b]]*9 + self.mapper[listb[b+1]]*50 + self.mapper[listb[b+100]] 
        num = num*27 + self.mapper[listc[c]]*9 + self.mapper[listc[c+1]]*50 + self.mapper[listc[c+100]] 
        return varkl



    

    
    def gamefunc (v1,v2):
        if v1 is 133:
            return v1*v2
        elif v1 is 0:
            return v1-v2
        else:
            return 0

    
