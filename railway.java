import java.io.*;
class railways
{
 String name,DOB,choice,city,username,password,repass,username1,password1,k,travelchoice;
 int choiceint,passlength,l=0,n=0,c=0,s=0,check=0,train,offern;
 char ch;
 String
regi[]={"delhi","mumbai","kolkata","chennai","amritsar","chandigar","lucknow","ahmedabad","patna","hyderabad",
"bangalore","cochin","agra"};

 void account()
 {

 String username1; int password1;

 do
 {
 c=0;
 System.out.println("login into your account");
 System.out.println("**********enter username***************:");
 username1=br.readLine());
 System.out.println("***************enter password*************:");
 password1=Integer.parseInt(br.readLine());
 if(!(username.equals(username1)&&password.equals(password1)))
 {
 System.out.println(" username & passwords match");
 c=1;
 else
 System.out.println(" username & passwords dont match");
 {
 }
 }while(c!=0);
 }

 void offer()
 {
 System.out.println("today's offer");
 offern=(int)(Math.random()*6);
 }
 {
 System.out.println("enter your mode of transport:" );
 String travel_choice=br.readLine();

 if(travel_choice.equals("train"))
 {
 System.out.println(" train package 1");

 {
 switch(train)
 {
 case 1:
 System.out.println("coach name = A1");
 break;
 case 2:
 System.out.println("coach name = A2");
 break;
 case 3:
 System.out.println("coach name = B1");
 break;
 case 4:
 System.out.println("coach name = sleeper");
 break;
 case 5:
 System.out.println("coach name = B2");
 break;
 case 6:
 System.out.println("coach name = A2");
 break;
 default: System.out.println("wrong choice");
 }
 n1=(int)((Math.random()*550)+300);
 System.out.println("cost= #"+n1);
 }
 System.out.println(" train package 2");
 {

 switch(train)
 {
 case 1:
 System.out.println("coach name = A1");
 break;
 case 2:
 System.out.println("coach name = A2");
 break;
 case 3:
 System.out.println("coach name = B1");
 break;
 case 4:
 System.out.println("coach name = sleeper");
 break;
 case 5:
 System.out.println("coach name = B2");
 break;
 case 6:
 System.out.println("coach name = A2");
 break;
 default:
 }
 n2=(int)((Math.random()*1000)+900);
 System.out.println("cost= #"+n2);
 }
 System.out.println(" train package 3");
 train=(int)(Math.random()*6);
 switch(train)
 {
 case 1:
 System.out.println("coach name = A1");
 break;
 case 2:
 System.out.println("coach name = A2");
 break;
 case 3:
 System.out.println("coach name = B1");
 break;
 case 4:
 System.out.println("coach name = sleeper");
 break;
 case 5:
 System.out.println("coach name = B2");
 break;
 case 6:
 System.out.println("coach name = A2");
 break;
 default:
 }
 n3=(int)((Math.random()*1000)+500);
 System.out.println("cost= $"+n3);
 System.out.println("enter your choice:");
 c=Integer.parseInt(br.readLine());
 switch(c)
 {
 case 1:
 s=s+n1;
 break;
 case 2:
 s=s+n2;
 break;
 case 3:
 s=s+n3;
 break;
 default:System.out.println("wrong choice");
 }
 }

 else
 {
 System.out.println("your choice is not present in our server ");

 }
 }

 void print()
 {
 System.out.println("final sum="+s);
 }
 public static void main()throws IOException
 {
 InputStreamReader isr= new InputStreamReader (System .in);
 BufferedReader br=new BufferedReader(isr);
 Raiways obj=new Railways();
 obj.account();
 obj.offer();

}
}
