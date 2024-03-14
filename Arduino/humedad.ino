int pin_Shumedad = A0;

void setup() {
    Serial.begin(9600);
}

void loop() {
    int humedad = analogRead(pin_Shumedad);
    Serial.println(humedad/10.23);
    delay(1000);
}

//Se divide por 10,23 para que el valor maximo (1023) este expresado en 100, para luego sacar promedios de los 3 sensores...