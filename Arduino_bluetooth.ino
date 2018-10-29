#include "SoftwareSerial.h"
SoftwareSerial serial_connection(2, 4);//Create a serial connection with TX and RX on these pins
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char inChar=-1;//Initialie the first character as nothing
int count=0;//This is the number of lines sent in from the python script
int i=0;//Arduinos are not the most capable chips in the world so I just create the looping variable once
int test_i = 0;

//String to store the different data
String previous_data_received = "";
String last_data_received = "";
String good_word = "";

//Variable of incrementation which allows to count the number of values received and to add the values to the tables
int j = 0;

//Table where the data is stored
String good_name[16];
String bad_name1[16];
String bad_name2[16];
String good_syllable[16];

//Variable which allows to change of the structure of program, there are three parts receive_data, game, send_data
int a = 0;

//Tables for the results 
int results_name[16]; //just score
String results_syllables[16]; //syllables + score

void setup()
{
  Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.
}
void loop()
{
  //While a == 0, the Arduino receive the data
  while(a == 0){
  //This will prevent bufferoverrun errors
  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script
  if(byte_count)//If there are any bytes then deal with them
  {
    Serial.println("Incoming Data");//Signal to the monitor that something is happening
    int first_bytes=byte_count;//initialize the number of bytes that we might handle. 
    int remaining_bytes=0;//Initialize the bytes that we may have to burn off to prevent a buffer overrun
    if(first_bytes>=BUFFER_SIZE-1)//If the incoming byte count is more than our buffer...
    {
      remaining_bytes=byte_count-(BUFFER_SIZE-1);//Reduce the bytes that we plan on handleing to below the buffer size
    }
    for(i=0;i<first_bytes;i++)//Handle the number of incoming bytes
    {
      inChar=serial_connection.read();//Read one byte
      if(int(inChar)<128 && int(inChar)>0){ //Check if the byte is in the ASCII table
        inData[i]=inChar;//Put it into a character string(array)
      }
    }
    inData[i]='\0';//This ends the character array with a null character. This signals the end of a string
    if((String(inData).length()>3 || isdigit(inData[0]) )&& String(inData)!="stop"){ //Check if inData contains many letters.
      //Store the data
      previous_data_received = last_data_received;
      last_data_received = inData;

      //Check if the data received the last time and the data of now is similary, if it is so we add the value to a table in function of the value of j
      if(previous_data_received == last_data_received){
          //Serial.println(inData);
         // test_i++;
          Serial.println(test_i);
          if(j<16){
            Serial.println(last_data_received);
            good_syllable[j] = last_data_received;
            //good_word = last_data_received;
            Serial.println("j vaut : " + String(j));
          }else if (j<32 && j > 15){
            Serial.println(last_data_received);
            Serial.println("j vaut : " + String(j-16));
            good_name[j-16] = last_data_received;
          }else if (j<48 && j > 31){
            Serial.println(last_data_received);
            Serial.println("j vaut : " + String(j-32));
            bad_name1[j-32] = last_data_received;
          }else /*if(j< 64 && j > 47)*/{
            Serial.println(last_data_received);
            Serial.println("j vaut : " + String(j-48));
            bad_name2[j-48] = last_data_received;
          }
      //Send a message to Pc to say the data is received
      serial_connection.println(last_data_received);
      j++;
      last_data_received = "";
      previous_data_received = "";
      }else{
        serial_connection.println("nothing");
        previous_data_received = "";
      }
      if(j==16){
        Serial.println("Les bonnes syllabes sont les suivantes : ");
        int y;
              for (y = 0; y < 16; y = y + 1) {
                Serial.println(good_syllable[y]);
              }
      }
      if(j==32){
        Serial.println("Les bons noms sont les suivants : ");
        int y;
              for (y = 0; y < 16; y = y + 1) {
                Serial.println(good_name[y]);
              }
      }
      if(j==48){
        Serial.println("Les mauvais noms 1 sont les suivants : ");
        int y;
              for (y = 0; y < 16; y = y + 1) {
                Serial.println(bad_name1[y]);
              }
      }
      if(j==64){
        Serial.println("Les mauvais noms 2 sont les suivantes : ");
        int y;
              for (y = 0; y < 16; y = y + 1) {
                Serial.println(bad_name2[y]);
              }
        a++;
      }
    }
    for(i=0;i<remaining_bytes;i++)//This burns off any remaining bytes that the buffer can't handle.
    {
      inChar=serial_connection.read();
    }
    serial_connection.flush();
    //Serial.println(inData);//Print to the monitor what was detected
    //serial_connection.println("Hello from Blue "+String(count));//Then send an incrmented string back to the python script
    //count++;//Increment the line counter
  }
  delay(200);//Pause for a moment 
  }
  //While a == 1, the Arduino play the game
  while( a== 1){
    Serial.print("jeu");
    a++;
  }
  //While(a == 2), the arduino sends the results to the computer
  while(a == 2){
    results_name[0] = 1;
    results_name[1] = 0;
    results_name[2] = 1;
    results_name[3] = 1;
    results_name[4] = 1;
    results_name[5] = 0;
    results_name[6] = 1;
    results_name[7] = 0;
    results_name[8] = 1;
    results_name[9] = 0;
    results_name[11] = 1;
    results_name[12] = 1;
    results_name[13] = 0;
    results_name[14] = 1;
    results_name[15] = 1;
    results_syllables[0] = "fa-1";
    results_syllables[1] = "fi-0";
    results_syllables[2] = "fu-1";
    results_syllables[3] = "fo-2";
    results_syllables[4] = "fa-1";
    results_syllables[5] = "fi-0";
    results_syllables[6] = "fu-1";
    results_syllables[7] = "fo-0";
    Serial.println("results");
    int z;
    for (z = 0; z < 16; z = z + 1) {
        serial_connection.print(String(results_name[z]));
        delay(200);
    }
    serial_connection.print("end");
    z = 0;
    for (z = 0; z < 9; z = z + 1) {
        serial_connection.print(String(results_syllables[z]));
        delay(200);
    }
    serial_connection.print("end");
  }
  
}
