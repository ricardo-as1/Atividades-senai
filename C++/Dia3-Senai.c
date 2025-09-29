// ================== Atividades: 15/09/2025 Senai ==================

#include <stdio.h>

int main() {
    // ================== Atividade 1: Maior número entre dois valores ==================
    /*
    int n1, n2;

    printf("Digite o primeiro número: ");
    scanf("%d", &n1);

    printf("Digite o segundo número: ");
    scanf("%d", &n2);

    if (n1 > n2) {
        printf("O maior número é: %d\n", n1);
    } else if (n2 > n1) {
        printf("O maior número é: %d\n", n2);
    } else {
        printf("Os números são iguais: %d\n", n1);
    }
    */

    // ================== Atividade 2: Verificar se o número é positivo, negativo ou zero ==================
    /*
    int numero;

    printf("Digite um número: ");
    scanf("%d", &numero);

    if (numero > 0) {
        printf("O número %d é positivo!\n", numero);
    } else if (numero < 0) {
        printf("O número %d é negativo!\n", numero);
    } else {
        printf("O número é zero!\n");
    }
    */

    // ================== Atividade 3: Identificar o sexo ==================
    /*
    char sexo;

    printf("Digite 'F' ou 'f' para Feminino e 'M' ou 'm' para Masculino: ");
    scanf(" %c", &sexo);

    if (sexo == 'M' || sexo == 'm') {
        printf("Sexo Masculino!\n");
    } else if (sexo == 'F' || sexo == 'f') {
        printf("Sexo Feminino!\n");
    } else {
        printf("Sexo Inválido!\n");
    }
    */

    // ================== Atividade 4: Identificar se a letra é vogal ou consoante ==================
    /*
    char letra;

    printf("Digite uma letra: ");
    scanf(" %c", &letra);

    letra = (letra >= 'a' && letra <= 'z') ? letra - ('a' - 'A') : letra;

    if (letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U') {
        printf("A letra digitada é Vogal!\n");
    } else {
        printf("A letra digitada é Consoante!\n");
    }
    */

    // ================== Atividade 5: Maior número entre três valores ==================
    /*
    int n1, n2, n3;

    printf("Digite o primeiro número: ");
    scanf("%d", &n1);

    printf("Digite o segundo número: ");
    scanf("%d", &n2);

    printf("Digite o terceiro número: ");
    scanf("%d", &n3);

    if (n1 >= n2 && n1 >= n3) {
        printf("O maior número é: %d\n", n1);
    } else if (n2 >= n1 && n2 >= n3) {
        printf("O maior número é: %d\n", n2);
    } else {
        printf("O maior número é: %d\n", n3);
    }
    */

    // ================== Atividade 6: Maior e menor número entre três valores ==================
    /*
    int n1, n2, n3, maior, menor;

    printf("Digite o primeiro número: ");
    scanf("%d", &n1);

    printf("Digite o segundo número: ");
    scanf("%d", &n2);

    printf("Digite o terceiro número: ");
    scanf("%d", &n3);

    if (n1 >= n2 && n1 >= n3) {
        maior = n1;
    } else if (n2 >= n1 && n2 >= n3) {
        maior = n2;
    } else {
        maior = n3;
    }

    if (n1 <= n2 && n1 <= n3) {
        menor = n1;
    } else if (n2 <= n1 && n2 <= n3) {
        menor = n2;
    } else {
        menor = n3;
    }

    printf("O maior número é: %d\n", maior);
    printf("O menor número é: %d\n", menor);
    */

    // ================== Atividade 7: Número correspondente ao dia da semana ==================
    /*
    int dia;

    printf("Digite um número de 1 a 7: ");
    scanf("%d", &dia);

    if (dia == 1) {
        printf("Domingo\n");
    } else if (dia == 2) {
        printf("Segunda-feira\n");
    } else if (dia == 3) {
        printf("Terça-feira\n");
    } else if (dia == 4) {
        printf("Quarta-feira\n");
    } else if (dia == 5) {
        printf("Quinta-feira\n");
    } else if (dia == 6) {
        printf("Sexta-feira\n");
    } else if (dia == 7) {
        printf("Sábado\n");
    } else {
        printf("Número inválido\n");
    }
    */

    return 0;
}
