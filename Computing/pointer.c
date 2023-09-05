# include <stdio.h>
# define STUDENT_NUMS 5

typedef struct{
    char name[20];
    float midterm;
    float final;
    int age;
    float total;
} Student;
// or we can do it like  :
// typedef struct Student Studebt;

void calcTotal(Student *s); //get pointer of Student type structure

int main(void){
    Student s[STUDENT_NUMS];
    for(int i=0;i<STUDENT_NUMS;i++){
        printf("Enter name, mid, final, age : ");
        scanf("%s %f %f %d", s[i].name, &s[i].midterm, &s[i].final, &s[i].age);
        // name은 이미 array이므로 &를 붙이지 않아도 주소가 전달됨
        calcTotal(&s[i]);
    }

    for(int i=0 ; i<STUDENT_NUMS ; i++){
        printf("name : %s, mid : %f, final : %f, age : %f, total : %d \n",
        s[i].name, s[i].midterm, s[i].final, s[i].age, s[i].total);
    }

    return 0;
}

void calcTotal(Student *s){
    s->total = s->midterm + s->final;
}