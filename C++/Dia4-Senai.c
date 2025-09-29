// ================== Atividades: 22/09/2025 Senai ==================

#include <stdio.h>

int main() {
    // ================== Atividade 1: Somatório de Números ==================
    /*
    int soma = 0, numero;

    for (int i = 1; i <= 5; i++) {
        printf("Digite o %dº número: ", i);
        scanf("%d", &numero);
        soma += numero;
    }
    printf("A soma dos 5 números é: %d\n", soma);
    */

    // ================== Atividade 2: Taboada ==================
    /*
    int numero;

    printf("Digite o número desejado para a taboada: ");
    scanf("%d", &numero);

    printf("Taboada do %d:\n", numero);

    for(int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", numero, i, numero * i);
    }*/

    // ================== Atividade 3: Validação de número ==================
    /*
    int numero;

    while (numero >= 0) {
        printf("Por favor, digite um número positivo(ou um negativo para sair): ");
        scanf("%d", &numero);

        if (numero >= 0) {
        printf("O número digitado é positivo: %d\n", numero);
        } else if (numero <= 0) {
            printf("O número digitado é negativo: %d\n", numero);
        }

    }*/

    // ================== Atividade 4: Avalia uma nota ==================
    /*
    int numero = 0;

    while (numero >= 0) {
        printf("Por favor, digite uma nota: ");
        scanf("%d", &numero);

        if (numero <= 10) {
        printf("O nota é válida!");
        } else {
            printf("O nota é inválida!");
        }
    }*/

    // ================== Atividade 5: Imprime números de 1 a 20 ==================
    /*
    int numero = 0;

    for(int numero = 0; numero <= 20; numero++) {
        printf("%d\n", numero);
    }
    for(int numero = 0; numero <= 20; numero++) {
        printf("%d, ", numero);
    }*/

    // ================== Atividade 6: Imprime números ímpares ==================
    /*
    int numero;

    for(int numero = 1; numero <= 50; numero++) {
        if (numero % 2 != 0) {
        printf("%d\n", numero);
        }
    }*/

  return 0;
}
