# include <stdio.h>
# define STUDENT_NUMS 5

// Arrays : memory efficient but hard to extend sizes
    // Array는 run-time stack(grows upwards)을 사용해서 메모리를 할당함.
    // Local variable들 저장하는 곳, 후입선출이라 매우 빠름
// Linked Lists : easy to extend sizes but not memory efficient(next/prev pointers)
    // Linked List는 heap(grows downwards)을 사용.
    // Global variable을 저장하는 곳, malloc()을 통해 메모리를 할당함. 

// 그래서 heap에는 malloc()을 통해 메모리를 할당하고, free()를 통해 메모리를 해제함.
    // allocation이 되지 않으면 null pointer를 반환.

typedef struct{
    char name[20];
    float midterm;
    float final;
    int age;
    float total;
} Student;

int main(void){
    //int asdf = malloc(sizeof(int));
    int *intPtr = malloc(sizeof(int));
    intPtr2 = (int*)malloc(sizeof(int)); // 이렇게도 할당 가능
    char *cPtr = malloc(sizeof(char));
    Student *sPtr = malloc(sizeof(Student));

    free(intPtr);
    free(intPtr2);
    free(cPtr);
    free(sPtr);
}


