int temp_val;
int tempPin = A2;

const int sensorIn = A1;
const int sensorIn_volt = A0;
int mVperAmp = 66;

double sensorValue=0;
double sensorValue1=0;
//int crosscount=0;
//int climbhill=0;
//double VmaxD=0;
//double VeffD;
//double Veff;

int FloatSensor1=A3;  
int FloatSensor2=A4;
          
int buttonState1 = 1; //reads pushbutton status 
int buttonState2 = 1; //reads pushbutton status

double volt = 0;
double Vrms = 0;

double Voltage = 0;
double VRMS = 0;
double AmpsRMS = 0;

double power=0;
double final_val=0;

void setup(){ 
 Serial.begin(9600);
 pinMode(A2,INPUT);
 pinMode(FloatSensor1, INPUT_PULLUP); 
pinMode(FloatSensor2, INPUT_PULLUP); 
}

void loop(){
  

 volt= getVPP1();
 Vrms= volt*2.9390845;    //3.38
 
 Voltage = getVPP();
 VRMS = (Voltage/2.0) *0.707; 
 AmpsRMS = (VRMS * 1000)/mVperAmp;
  
/////////////////........OIL LEVEL.........//////////////////////////////
  buttonState1 = digitalRead(FloatSensor1); 
 
 buttonState2 = digitalRead(FloatSensor2);
 
 //////////////........TEMPRATURE LEVEL....////////////////////////////
 temp_val = analogRead(tempPin);
float temp_val = analogRead(A2);
float mv = ( temp_val/1024.0)*5000;
float cel = mv/10;



////////////.........POWER............//////////////////////////

power= (Vrms)*AmpsRMS;

Serial.print(power);
Serial.print(",");
Serial.print(AmpsRMS);
Serial.print(","); 
Serial.print(Vrms);
Serial.print(",");
Serial.print(cel);
Serial.print(",");
Serial.print( buttonState1);
Serial.print(",");
Serial.println( buttonState2);

}

///////////////........VOLTAGE LEVEL.......////////////////////////////
 
 float getVPP1()
{
  float result;
  
  int readValue;             //value read from the sensor
  int maxValue = 0;          // store max value here
  int minValue = 1024;          // store min value here
  
   uint32_t start_time = millis();
   while((millis()-start_time) < 1000) //sample for 1 Sec
   {
       readValue = analogRead(sensorIn_volt);
       // see if you have a new maxValue
       if (readValue > maxValue) 
       {
           /*record the maximum sensor value*/
           maxValue = readValue;
       }
       if (readValue < minValue) 
       {
           /*record the maximum sensor value*/
           minValue = readValue;
       }
   }  
   // Subtract min from max
   result = ((maxValue - minValue) * 5.0)/1024.0;  
   return result;
   
 }

/////////////////..........CURRENT LEVEL..........///////////////
float getVPP()
{
  float result;
  
  int readValue;             //value read from the sensor
  int maxValue = 0;          // store max value here
  int minValue = 1024;          // store min value here
  
   uint32_t start_time = millis();
   while((millis()-start_time) < 1000) //sample for 1 Sec
   {
       readValue = analogRead(sensorIn);
       // see if you have a new maxValue
       if (readValue > maxValue) 
       {
           /*record the maximum sensor value*/
           maxValue = readValue;
       }
       if (readValue < minValue) 
       {
           /*record the maximum sensor value*/
           minValue = readValue;
       }
   }
   
   // Subtract min from max
   result = ((maxValue - minValue) * 5.0)/1024;
      
   return result;
 }
