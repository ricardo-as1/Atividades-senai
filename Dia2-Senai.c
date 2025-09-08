// ================== Atividades: 08/09/2025 Senai ==================

#include <stdio.h>

int main() {
    // ================== Atividade 1: Salario Mensal ==================
    /*
    int main() {
    float valorHora, horasPorDia, diasTrab, salarioMensal;

    printf("Informe quanto você ganha por hora: ");
    scanf("%f", &valorHora);

    printf("Quantas horas você trabalha por dia? ");
    scanf("%f", &horasPorDia);

    printf("Quantos dias você trabalha no mês? ");
    scanf("%f", &diasTrab);

    salarioMensal = valorHora * horasPorDia * diasTrab;

    printf("O seu salário no mês é: R$ %.2f \n", salarioMensal);

    return 0;
    }

    */

    // ================== Atividade 2: Calculo do peso M & F ==================
    /*
    int main() {
    float H, kg;
    char sexo;

    printf("Informe sua altura em metros: ");
    scanf("%f", &H);

    printf("Informe seu sexo: ");
    scanf(" %c", &sexo);

    if (sexo == 'M' || sexo == 'm') {
        kg = (72.7 * H) - 58;
        printf("Peso ideal do homem é: %.2f\n", kg);
    } else if(sexo == 'F' || sexo == 'f') {
        kg = (62.1 * H) - 44.7;
        printf("Pesoal ideal da mulher é: %.2f\n", kg);
    } else {
        printf("Sexo inválido!\n");
    }

    return 0;
    }
    */

    // ================== Atividade 3: Calculo de excesso de peso ==================
    /*
    int main() {
    float peso, excesso, multa;

    printf("Informe o peso dos peixes(em quilos): ");
    scanf("%f", &peso);

    if (peso > 50) {
        excesso = peso - 50;
        multa = excesso * 4.0;
        printf("Excesso de peso: %.2f quilos\n", excesso);
        printf("Multa a ser paga: %.2f$\n", multa);
    } else {
        printf("Não há excesso de peso. Nenhuma multa será aplicada!");
    }

    return 0;
    }
    */

    // ================== Atividade 4: Calculo de Salario + Descontos ==================
    /*
    int main() {
    float valorHora, hrTrab, valorLiq, salarioBruto, sindicato, IR, INSS;

    printf("Quanto você ganha por hora: ");
    scanf("%f", &valorHora);

    printf("Número de horas trabalhadas: ");
    scanf("%f", &hrTrab);

    salarioBruto = valorHora * hrTrab;
    IR = salarioBruto * 0.11;
    INSS = salarioBruto * 0.08;
    sindicato = salarioBruto * 0.05;
    valorLiq = salarioBruto - ( IR + INSS + sindicato );
    
    printf("\nSalário Bruto     : R$%.2f\n", salarioBruto);
    printf("IR                : R$%.2f\n", IR);
    printf("INSS              : R$%.2f\n", INSS);
    printf("Sindicato         : R$%.2f\n", sindicato);
    printf("Valor Liquido     : R$%.2f\n", valorLiq);

    return 0;
    }
    */

    return 0; // Necessário para o main, mesmo que todas as atividades estejam comentadas
}