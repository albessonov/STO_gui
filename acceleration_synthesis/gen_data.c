
#include <time.h>

/* Include Files */
#include "gen_data.h"

input_val in;
output_val out;
massive_val mas;

file_write f_w;

void mask(void);

void gen_data(void)
{

    printf("time = %f\n",out.Timer);

    // Маска
    mask();

    // Генератор
    if ((out.Timer >= mas.time_start) && (out.Timer <= mas.time_end)){

        // Ares
        //out.Ares = mas.A_min + (mas.A_max - mas.A_min) * (rand() % 2);
        out.Ares = mas.A_min + (mas.A_max - mas.A_min) * ((float)rand()/RAND_MAX);

        if (out.Ares == 0) {

            out.Ax = 0;
            out.Ay = 0;
        } else {

            // Ax
            out.Ax = mas.Axy_min + (mas.Axy_max - mas.Axy_min) * ((float)rand()/RAND_MAX);


            while (out.Ax > out.Ares) {
                // Ares
                out.Ares = mas.A_min + (mas.A_max - mas.A_min) * (rand() % 2);

                // Ax
                out.Ax = mas.Axy_min + (mas.Axy_max - mas.Axy_min) * (rand() % 2);
                while (out.Ax == 0) {
                    out.Ax = mas.Axy_min + (mas.Axy_max - mas.Axy_min) * (rand() % 2);
                }
            }

            // Ay
            out.Ay = sqrt(pow(out.Ares,2)-pow(out.Ax,2));

            // Определение стороны удара
            out.Ax *= mas.coef_Ax;
            out.Ay *= mas.coef_Ay;

        }
    }

    //printf("Ax = %f, Ay = %f, Ares = %f\n\n",out.Ax,out.Ay,out.Ares);


    return 0;
}

void init_data(void)
{

    // Инициализация
    memset(&mas,0,sizeof(mas));
    memset(&out,0,sizeof(out));

      // Сдвиг временных интервалов в зависимости от задержек
    in.time_start_max += in.time_before;
    in.time_end_max += in.time_before;
    in.time_start_min += in.time_before;
    in.time_end_min += in.time_before;

    mas.time_start = 0;     // начало временного интервала // ms
    mas.time_end = in.time_end_max;


    // Маска Ares
    mas.tg_up_max = (in.Limit_Ares + in.Ares_range)/in.time_up_max;
    mas.tg_down_max = -(in.Limit_Ares + in.Ares_range)/in.time_down_max;

    mas.tg_up_min = in.Limit_Ares/in.time_up_min;
    mas.tg_down_min = -in.Limit_Ares/in.time_down_min;

    // Маска
    if (strcmp(in.side, "front") == 0) {
            mas.coef_Ax = -1;
            mas.coef_Ay = -1;
    } else if (strcmp(in.side, "left") == 0) {
            mas.coef_Ax = 1;
            mas.coef_Ay = -1;
    } else if (strcmp(in.side, "right") == 0) {
            mas.coef_Ax = -1;
            mas.coef_Ay = 1;
    } else if (strcmp(in.side, "rear") == 0) {
            mas.coef_Ax = 1;
            mas.coef_Ay = 1;
    }

    return 0;
}

void mask(void)
{
    // Маска Ares

    // A_max

    if ((out.Timer > in.time_start_max + in.time_up_max) && (out.Timer < in.time_end_max - in.time_down_max)) {
        mas.A_max = in.Limit_Ares + in.Ares_range;

    } else if ((out.Timer >= in.time_start_max) && (out.Timer <= in.time_start_max + in.time_up_max)) {
        mas.A_max = mas.tg_up_max * (out.Timer - in.time_start_max);

    } else if ((out.Timer >= in.time_end_max - in.time_down_max) && (out.Timer <= in.time_end_max)) {
        mas.A_max = mas.tg_down_max * (out.Timer - (in.time_end_max - in.time_down_max)) + in.Limit_Ares + in.Ares_range;

    }


    // A_min
    if ((out.Timer > in.time_start_min + in.time_up_min) && (out.Timer < in.time_end_min - in.time_down_min)) {
        mas.A_min = in.Limit_Ares;

    } else if ((out.Timer >= in.time_start_min) && (out.Timer <= in.time_start_min + in.time_up_min)) {
        mas.A_min = mas.tg_up_min * (out.Timer - in.time_start_min);

    } else if ((out.Timer >= in.time_end_min - in.time_down_min) && (out.Timer <= in.time_end_min)) {
        mas.A_min = mas.tg_down_min * (out.Timer - (in.time_end_min - in.time_down_min)) + in.Limit_Ares;

    }


    if (mas.A_min < 0) {
        mas.A_min = 0;
    }

    if (mas.A_max < 0) {
        mas.A_max = 0;
        mas.A_min = 0;
    }



    // Маска Ax and Ay

    mas.Axy_max = mas.A_max/sqrt(2);
    mas.Axy_min = mas.A_min/sqrt(2);

    return 0;
}

