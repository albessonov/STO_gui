/* Include Files */
#include <stddef.h>
#include <stdlib.h>

/* Type Definitions */
#include <stdio.h>
#include <stdbool.h>

#include <locale.h>

#include <stdlib.h>


// Структура ввода
typedef struct {

    // Параметры коридора
    float Limit_Ares, Ares_range;
    char side[10];

    // Верхняя трапеция
    float time_start_max,time_end_max, time_up_max,time_down_max;

    // Нижняя трапеция
    float time_start_min,time_end_min, time_up_min,time_down_min;

    // частота дискретизации и задержка вначале
    float time_step,time_before;


} input_val;

// Структура вывода
typedef struct {

    float Timer,Ax,Ay, Ares;
    bool again;

} output_val;

// Структура массивов
typedef struct {

    float counter;                                          // счетчик
    float time_start,time_end;                              // временные рамки

    float tg_up_max,tg_down_max, tg_up_min,tg_down_min;     // наклон коридора

    float A_max,A_min, Axy_max,Axy_min;                     // пределы коридоров
    float coef_Ax,coef_Ay;                                  // направление удара

} massive_val;

// Структура массивов
typedef struct {

    char * line[1000];      // строка для записи
    char acc_str[10];       // доп строка для записи в файл

    // Запись в файл
    char * filename[20];    // название файла
    FILE *fp;               // файл

} file_write;


// External
extern input_val in;
extern output_val out;
extern massive_val mas;

extern file_write f_w;

/* Function Declarations */
extern void gen_data(void);
extern void init_data(void);
