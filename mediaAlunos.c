#include <stdio.h>

int main() {
    int n;
    char nome[30];
    float n1, n2, n3, mediaTurma;

    scanf("%d",&n);


    for (int i = 0; i < n; i++){
        scanf("%s %f %f %f", nome, &n1, &n2, &n3);

        float media = (n1 + n2 + n3)/3;
        printf("%s - Media: %.2f - ", nome, media);
        if(media >= 5){
            printf("APROVADO\n");
        }else if(media >= 3){
            printf("RECUPERACAO\n");
        }else{
            printf("REPROVADO\n");
        }
    } 

    return 0;
    
}