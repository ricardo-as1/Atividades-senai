frutas = ["Maçã", "Banana", "Melão", "Melancia", "Coco"]

print("Frutas na lista inicial:")
for fruta in frutas:
    print(fruta)

print("\nAdicione 3 frutas à lista:")
for i in range(3):
    append_fruta = input(f"Digite o nome da fruta {i+1}/3: ").strip().capitalize()
    if append_fruta:
        frutas.append(append_fruta)

print("\n--- Lista Final ---")
print(frutas)
