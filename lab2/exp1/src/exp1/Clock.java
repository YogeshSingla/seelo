/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exp1;

/**
 *
 * @author Student
 */
public class Clock implements SecondObserver {
    
    //instance variables
    int hour;
    int minute;
    int second;
    boolean isAM;
    /**
     * @param args the command line arguments
     */
    
    public Clock(){
        this.hour = 0;
        this.minute = 0;
        this.second = 0;
        this.isAM = true;
    }
    
    public Clock(int hour, boolean isAM){
        this.hour = hour;
        this.minute = 0;
        this.second = 0;
        this.isAM = isAM;
    }
    
    public Clock(int hour,int minute, int second, boolean isAM){
        this.hour = hour;
        this.minute = minute;
        this.second = second;
        this.isAM = isAM;
    }
    
    public int getHours(){
        return hour;
    }
    public int getMinutes(){
        return minute;
    }
    public int getSeconds(){
        return second;
    }
    
    public void setTime(int h, int m, int s, boolean isAM){
        this.hour = h;
        this.minute = m;
        this.second = s;
        this.isAM = isAM;
    }
    public void tick(){
        int tempsecond = this.second + 1;
        this.second = (this.second + 1)%60;
        this.minute = this.minute + tempsecond/60;
        this.hour = this.hour + this.minute/60;
        this.minute = this.minute%60;
        //print(this);
        if(this.hour == 12){
            //System.out.println(this.isAM);
            this.isAM = !this.isAM;
            //System.out.println(this.isAM);
        }
        this.hour = this.hour%12;
        
        if(this.isAM == false && this.hour == 0)
            this.hour = 12;
        
        print(this);
    }
    
    public static void print(Clock toprint){
        if(toprint.isAM)
            System.out.println(toprint.hour+":" + toprint.minute + ":" +toprint.second + " AM");
        else
            System.out.println(toprint.hour+":" + toprint.minute + ":" +toprint.second + " PM");
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.println("Clock");
        
        Clock c1 = new Clock();
        Clock c2 = new Clock(12,true);
        Clock c3 = new Clock(11,59,58,false);
        Clock c4 = new Clock(11,59,58,true);
        Clock c5 = new Clock(05,34,15,true);
        
        print(c1);
        print(c2);
        print(c3);
        
        //c2.tick();
        //c2.tick();
        System.out.println("Testing c3");
        c3.tick();
        c3.tick();
        c3.tick();
        
        System.out.println("Testing c4");
        c4.tick();
        c4.tick();
        c4.tick();
        
        System.out.println("Testing c5");
        c5.tick();
        c5.tick();
        c5.tick();
    }
    
}
