#include <stdio.h>

// http://www.tcpschool.com/c/c_struct_intro  그리고 
// https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ruvendix&logNo=220904838279 를 참조함.

struct book{
    char title[30];
    char author[30];
    int price;
};

//Similarly, one can define a alias of a structure with typedef : 
//이게 되는 이유는 typedef {재정의할 자료형} {재정의된 이름}; format이기 때문.
typedef struct{
    char name[20];
    float height;
    float weight;
    int age;
} Person;

int main(void){
    struct book book1 = {
        "HTML & CSS", "george", 20
    };
    struct book book2 = {
        .title = "java", .price = 30
    };
    
    printf("first book's title is %s, author is %s, price is %d. \n",
    book1.title, book1.author, book1.price);
    printf("second book's title is %s, author is %s, price is %d. \n",
    book2.title, book2.author, book2.price);

    //Person = struct type의 Per
    Person p1 = {
        "george", 178.8, 70.1, 28
    };
    Person p2 = {
        .name="sam", .height=180.5, .age=30
    };

    printf("p1 : name=%s, height and weight = %f, %f, age = %d \n", 
    p1.name, p1.height, p1.weight, p1.age);
    printf("p2 : name=%s, height and weight = %f, %f, age = %d \n", 
    p2.name, p2.height, p2.weight, p2.age);

    return 0;
}