from symptoms import SYMPTOMS
from recommender import get_remedy

def display_symptoms():
    print("-----SYMPTOM CHECKER-----")
    print("Select symptoms by entering their numbers (use comma): \n")
    print()
    for i, symptom in enumerate(SYMPTOMS, start=1):
        print(f" {i:2}. {symptom}")
    print()

def get_user_selection()-> list[str]:
    while True:
        raw = input("Enter numbers: ")
        try:
            indices = [int(x.strip()) for x in raw.split(",")]
            selected = []
            for idx in indices:
                if 1 <= idx <= len(SYMPTOMS):
                    selected.append(SYMPTOMS[idx - 1])
                else:
                    print(f"Skipping invalid number: {idx}")
            if selected:
                return selected
            else:
                print("No valid symptom selcted. Try again.")
        except ValueError:
            print("Invalid input. please enter number separated by comma:")

def main():
    display_symptoms()
    selected = get_user_selection()

    print(f"\n You selected: {', '.join(selected)}")
    print("\n Fetching remedy recommendation....\n")

    remedy = get_remedy(selected)

    print("=" * 40)
    print("Temporary remedy recommendation")
    print("=" * 40)
    print(remedy)
    print(" diye gaye nuske kisi v prakaar ka daawa nhi karte ek baar kisi Doctor se sampark jarur kare ")

if __name__ == "__main__":
    main()
    