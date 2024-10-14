#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <locale.h>
#include <stdint.h>

/* Include Files */
#include "gen_data.h"

#define X 0
#define Y 1
#define CRC_POLY  0x12F
#define SPI_DATA_LEN_BITS 32
#define CRC_SPI_SEED 0xFF
#define CRC_LEN 8
#define MSG_LEN 32
#define CRC_SEED 0xFF
#define MAX_CRC 0xFF
#define MAX_UINT64_T 0xFFFFFFFFFFFFFFFF
void write_to_file(void);
static uint32_t form_acc(float accel56eration,bool axis);
static uint8_t CRC8(uint32_t SPI_data);

static float deform_acc(float acceleration);

int main(int argc, char **argv)
{
    if(argc<13)
    {
        printf("Usage: gen2 arg1 arg2 ... arg14\n");
        printf("arg1-Limit_ares\n");
        printf("arg2-Ares_range\n");
        printf("arg3-side of collision(front/left/right/rear)\n");
        printf("arg4-time_start_max\n");
        printf("arg5-time_end_max\n");
        printf("arg6-time_up_max\n");
        printf("arg7-time_down_max\n");
        printf("arg8-time_start_min\n");
        printf("arg9-time_end_min\n");
        printf("arg10-time_up_min\n");
        printf("arg11-time_down_min\n");
        printf("arg12-time step(in ms). must be 0.5 to do tests with STO\n");
        printf("arg14-time before collision(in ms)\n");
        printf("arg14-name_of_output_file.csv\n");
    }
    bool write_on = true;
    // Параметры коридора
    in.Limit_Ares = atof(argv[1]); //предельное (минимальное) значение для ускорения // g
    in. Ares_range = atof(argv[2]); //ширина коридора (ускорение) // g

    strcpy(in.side,argv[3]); // front/left/right/rear

    // Верхняя трапеция
    in.time_start_max = atof(argv[4]);  // начало коридора  // ms
    in.time_end_max = atof(argv[5]);   // конец коридора  // ms
    in.time_up_max = atof(argv[6]);	// ширина коридора (время) // ms  < (time_end - time_start)/2/(1+Limit_Ares/(Limit_Ares+Ares_range))
    in.time_down_max = atof(argv[7]);

    // Нижняя трапеция
    in.time_start_min =atof(argv[8]);  // начало коридора  // ms
    in.time_end_min = atof(argv[9]);   // конец коридора  // ms
    in.time_up_min = atof(argv[10]);	// ширина коридора (время) // ms  < (time_end - time_start)/2/(1+Limit_Ares/(Limit_Ares+Ares_range))
    in.time_down_min = atof(argv[11]);


    // time range
    in.time_step = atof(argv[12]);                                     // временной шаг // ms
    in.time_before = atof(argv[13]);                                    // задержкка перед импульсом в мс

    if (write_on) {
        // Запись в файл
        strcpy(f_w.filename,argv[14]);
        f_w.fp = fopen(f_w.filename, "w");

        fputs("ref_X;ref_Y;acc_X;acc_Y;deform_X;deform_Y;time\n", f_w.fp);
    }

    // Алгоритм
    out.again = false;
    init_data();
    while (out.again == false) {

        // Таймер
        out.Timer = mas.time_start + in.time_step * mas.counter;

        // Генерация данных по маске
        gen_data();

        mas.counter += 1;

        if (write_on) {
            // Путь к файлу
            snprintf(f_w.acc_str, sizeof f_w.acc_str,"%f",out.Ax);
            strcpy(f_w.line,f_w.acc_str);
            strcat(f_w.line,";");
            snprintf(f_w.acc_str, sizeof f_w.acc_str,"%f",out.Ay);
            strcat(f_w.line,f_w.acc_str);
            strcat(f_w.line,";");

            snprintf(f_w.acc_str, sizeof f_w.acc_str,"%X",form_acc(out.Ax,X));
            strcat(f_w.line,f_w.acc_str);
            strcat(f_w.line,";");
            snprintf(f_w.acc_str, sizeof f_w.acc_str,"%X",form_acc(out.Ay,Y));
            strcat(f_w.line,f_w.acc_str);
            strcat(f_w.line,";");


            snprintf(f_w.acc_str, sizeof f_w.acc_str,"%f",deform_acc(out.Ax));
            strcat(f_w.line,f_w.acc_str);
            strcat(f_w.line,";");
            snprintf(f_w.acc_str, sizeof f_w.acc_str,"%f",deform_acc(out.Ay));
            strcat(f_w.line,f_w.acc_str);
            strcat(f_w.line,";");

            snprintf(f_w.acc_str, sizeof f_w.acc_str,"%f",out.Timer);
            strcat(f_w.line,f_w.acc_str);
            strcat(f_w.line,"\n");

            // записываем строку
            fputs(f_w.line, f_w.fp);
        }

        // делать ли остановку?
        if (out.Timer == mas.time_end) {
            out.again = true;
        } else {
            out.again = false;
        }

    }


    if (write_on) {
        fclose(f_w.fp);
        printf("File has been written\n");
    }

    return 0;
}


static float deform_acc(float acceleration)
{
    return round(327.36f*acceleration)/327.36f;  // 327.36

}


static uint32_t form_acc(float acceleration,bool axis)
{
	uint8_t valH0,valL0,valL,valH,B0,B1,B2,B3;
	int16_t acc_val=round(327.36f*acceleration);
	uint32_t formed_acceleration;
	uint8_t RCOMMAND0x00=0b10000100;
    uint8_t RCOMMAND0x02=0b10100100;
	uint8_t RCOMMAND;
	if(acc_val>=0)
	     {
          valL0 = (uint8_t) ((acc_val<<4) & 0x00ff);
          valH0 = (uint8_t) (((acc_val<<4) & 0xff00) >> 8);
          valL=valL0;
          valH=valH0;
	     }
	     else
	     {
          valL0 = (uint8_t) (((-acc_val)<<4) & 0x00ff);
          valH0 = (uint8_t) (((((-acc_val)<<4) & 0xff00) >> 8));
          valL=~valL0+1;
          valH=~valH0;
	     }
  if(axis==X) RCOMMAND=RCOMMAND0x00;
  else RCOMMAND=RCOMMAND0x02;
  B0=(RCOMMAND|(valH>>6));
  B1=((valH<<2)|(valL>>6));
  B2=(valL<<2);
  B3=CRC8((((uint32_t)B0)<<24)|(((uint32_t)B1)<<16)|(((uint32_t)B2)<<8));
	formed_acceleration=(((uint32_t)B0)<<24)|(((uint32_t)B1)<<16)|(((uint32_t)B2)<<8)|((uint32_t)B3);
	return formed_acceleration;
}

static uint8_t CRC8(uint32_t SPI_data)
{
	uint64_t mask = MAX_UINT64_T - MAX_CRC;
	uint64_t rem = (uint64_t)((((uint64_t)SPI_data) | (((uint64_t)CRC_SEED) << MSG_LEN)) & mask);
	uint64_t divider = ((uint64_t)CRC_POLY) << (MSG_LEN - 1);

	for (uint16_t i = MSG_LEN + CRC_LEN; i > 0; i--) //32 = 4*8
	{
		if (((rem >> (i - 1)) & 0x01) != 0)
		{
			rem ^= divider;
		}
		divider >>= 1;
		if ((rem & mask) == 0) //end of calc
		{
			break;
		}
	}
	// Return 8-bit CRC calculated
	return (uint8_t)(rem & MAX_CRC);
}
