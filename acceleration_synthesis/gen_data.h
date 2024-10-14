/* Include Files */
#include <stddef.h>
#include <stdlib.h>

/* Type Definitions */
#include <stdio.h>
#include <stdbool.h>

#include <locale.h>

#include <stdlib.h>


// ��������� �����
typedef struct {

    // ��������� ��������
    float Limit_Ares, Ares_range;
    char side[10];

    // ������� ��������
    float time_start_max,time_end_max, time_up_max,time_down_max;

    // ������ ��������
    float time_start_min,time_end_min, time_up_min,time_down_min;

    // ������� ������������� � �������� �������
    float time_step,time_before;


} input_val;

// ��������� ������
typedef struct {

    float Timer,Ax,Ay, Ares;
    bool again;

} output_val;

// ��������� ��������
typedef struct {

    float counter;                                          // �������
    float time_start,time_end;                              // ��������� �����

    float tg_up_max,tg_down_max, tg_up_min,tg_down_min;     // ������ ��������

    float A_max,A_min, Axy_max,Axy_min;                     // ������� ���������
    float coef_Ax,coef_Ay;                                  // ����������� �����

} massive_val;

// ��������� ��������
typedef struct {

    char * line[1000];      // ������ ��� ������
    char acc_str[10];       // ��� ������ ��� ������ � ����

    // ������ � ����
    char * filename[20];    // �������� �����
    FILE *fp;               // ����

} file_write;


// External
extern input_val in;
extern output_val out;
extern massive_val mas;

extern file_write f_w;

/* Function Declarations */
extern void gen_data(void);
extern void init_data(void);
