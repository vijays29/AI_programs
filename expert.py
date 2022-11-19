from experta import *
import yaml
with open("disease/disease_symptoms.yaml", "r") as f:
    (
        SYMPTOMS,
        SYMPTOM_QUERY,
        DISEASE_SYMPTOMS 
    ) = yaml.full_load(f).values()
DISEASE_FACTS = {
    disease: [
        Fact(**{symptom: "yes" if symptom in disease_symptoms else "no"})
        for symptom in SYMPTOMS
    ]
    for disease, disease_symptoms in DISEASE_SYMPTOMS.items()
}
hash_line = "\n"+"# "*50+"\n"
class MedicalExpert(KnowledgeEngine):
    username = "MR.TESTER"
    response = {}
    def declare_symptom_response(self,symptom):
        self.response[symptom]=input(
            f"\nDo you {SYMPTOM_QUERY[symptom]}?\nPlease type Yes/No :").strip().lower()
        self.declare(Fact(**{symptom:self.response[symptom]}))
    def declare_disease(self,disease):
        self.declare(Fact(disease=disease))
    @DefFacts()
    def initialization(self):
        response = input(
            "Hi! I am Mr.Expert.\n\n"
            "You can get yourself diagnosed here free of cost!\n"
            "I will ask you 10 questions.\n\n"
            "Do you want to get diagonised?\n"
            "Please type Yes/No :"
        ).strip().lower()
        yield Fact(findDisease= response)
    
    @Rule(Fact(findDisease="yes"), NOT(Fact(name=W())), salience=1000)
    def ask_name(self):
        self.username = input("\nWhat's your name?") or self.username
        self.declare(Fact(name=self.username))
    

    @Rule(Fact(findDisease="yes"), NOT(Fact(chest_pain=W())), salience=995)
    def hasChestPain(self):
        self.declare_symptom_response('chest_pain')

    @Rule(Fact(findDisease="yes"), NOT(Fact(cough=W())), salience=985)
    def hasCough(self):
        self.declare_symptom_response('cough')

    @Rule(Fact(findDisease="yes"), NOT(Fact(fainting=W())), salience=975)
    def hasFainting(self):
        self.declare_symptom_response('fainting')

    @Rule(Fact(findDisease="yes"), NOT(Fact(fatigue=W())), salience=970)
    def hasFatigue(self):
        self.declare_symptom_response('fatigue')

    @Rule(Fact(findDisease="yes"), NOT(Fact(headache=W())), salience=965)
    def hasHeadache(self):
        self.declare_symptom_response('headache')

    @Rule(Fact(findDisease="yes"), NOT(Fact(back_pain=W())), salience=955)
    def hasBackPain(self):
        self.declare_symptom_response('back_pain')

    @Rule(Fact(findDisease="yes"), NOT(Fact(sunken_eyes=W())), salience=950)
    def hasSunkenEyes(self):
        self.declare_symptom_response('sunken_eyes')

    @Rule(Fact(findDisease="yes"), NOT(Fact(fever=W())), salience=945)
    def hasFever(self):
        self.declare_symptom_response('fever')

    @Rule(Fact(findDisease="yes"), NOT(Fact(sore_throat=W())), salience=940)
    def hasSoreThroat(self):
        self.declare_symptom_response('sore_throat')

    @Rule(Fact(findDisease="yes"), NOT(Fact(restlessness=W())), salience=935)
    def hasRestlessness(self):
        self.declare_symptom_response('restlessness')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Covid"])
    def covid(self):
        self.declare_disease('Covid')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Alzheimers"])
    def alzheimers(self):
        self.declare_disease('Alzheimers')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Asthma"])
    def asthma(self):
        self.declare_disease('Asthma')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Diabetes"])
    def diabetes(self):
        self.declare_disease('Diabetes')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Epilepsy"])
    def epilepsy(self):
        self.declare_disease('Epilepsy')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Glaucoma"])
    def glaucoma(self):
        self.declare_disease('Glaucoma')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Heart Disease"])
    def heartDisease(self):
        self.declare_disease('Heart Disease')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Heat Stroke"])
    def heatStroke(self):
        self.declare_disease('Heat Stroke')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Hyperthyroidism"])
    def hyperthyroidism(self):
        self.declare_disease('Hyperthyroidism')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Hypothermia"])
    def hypothermia(self):
        self.declare_disease('Hypothermia')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Jaundice"])
    def jaundice(self):
        self.declare_disease('Jaundice')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Sinusitis"])
    def sinusitis(self):
        self.declare_disease('Sinusitis')

    @Rule(Fact(findDisease="yes"), *DISEASE_FACTS["Tuberculosis"])
    def tuberculosis(self):
        self.declare_disease('Tuberculosis')

    @Rule(Fact(findDisease="yes"), NOT(Fact(disease=W())), salience=-1)
    def unmatched(self):
        self.declare_disease('unknown')

    @Rule(Fact(findDisease="yes"), Fact(disease=MATCH.disease), salience=1)
    def getDisease(self, disease):
        if(disease == 'unknown'):
            yes_symptoms = {
                symptom 
                for symptom,response in self.response.items() 
                if response == "yes"
                 }
            disease = max(
                DISEASE_SYMPTOMS,
                key=lambda x: len(DISEASE_SYMPTOMS.get(x) & yes_symptoms)
            )
            print('\nWe checked the following symptoms:', *SYMPTOMS, sep="\n")
            print('\nSymptoms found in the patient are:',
                  *yes_symptoms or [None], sep="\n")
            if len(DISEASE_SYMPTOMS[disease] & yes_symptoms) == 0:
                print("\nNo diseases found.You are healthy!")
                return
            else:
                print(
                    "\nWe are unable to tell you the "
                    "exact disease with confidence."
                    "But we believe that you suffer from :",
                    disease
                )
        else:
            print('\nThe most probable illness you are suffering from is:', disease)
        self.print_disease_info(disease)

    def print_disease_info(self, disease):
        print(hash_line)
        print(f'Some info about {disease}:\n')
        with open("disease/disease_descriptions/" + disease + ".txt", "r") as f:
            print(f.read().strip())
        print(hash_line)
        print(
            f'No need to worry {self.username}. '
            'We even have some preventive measures for you!\n'
        )
        with open("disease/disease_treatments/" + disease + ".txt", "r")as f:
            print(f.read().strip())
        print(hash_line)

if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()