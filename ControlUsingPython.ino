
const int pin1=9;
const int pin2=10;
const int pin3=11;
int value=0;

void setup() 
   { 
      Serial.begin(9600); 
      pinMode(pin1, OUTPUT);
      digitalWrite (pin1, HIGH);
      pinMode(pin2, OUTPUT);
      digitalWrite (pin2, HIGH);
      pinMode(pin3, OUTPUT);
      digitalWrite (pin3, HIGH);
      Serial.println("Connection established...");
   }
 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     
     if (value == '1')
        digitalWrite (pin1, LOW);
     else if (value == '0')
        digitalWrite (pin1, HIGH);
     
     if (value == '3')
        digitalWrite (pin2, LOW);
     else if (value == '2')
        digitalWrite (pin2, HIGH);

     if (value == '5')
        digitalWrite (pin3, LOW);
     else if (value == '4')
        digitalWrite (pin3, HIGH);
   }
