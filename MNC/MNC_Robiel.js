// Date: 2021-09-30
// Creator: Robiel Tesfazghi


// Description:
// je commence par le nombre 100 000 000 et je l'incrémente de 1 jusqu'à ce que je trouve un nombre divisible par 3, 5, 7 et 9.
// Je convertirai le nombre en une chaîne de caractères, puis en un tableau de chiffres.
// Je vais créer un nouvel array pour stocker l'encodage des chiffres.
// Je vais parcourir le tableau de chiffres et vérifier si le chiffre est déjà apparu auparavant.
//si Oui, j'ajouterai l'encodage au nouveau tableau.
//Si Non, je vais ajouter le chiffre à un dictionnaire et ajouter l'encodage au nouveau tableau.
// Je joindrai le nouveau tableau à une chaîne de caractères et j'afficherai les résultats.

// trouver un nombre divisible par 3, 5, 7 et 9 supérieur à 100 000 000
function findNumber() {
    for (let n = 100000000;; n++) {
        if (n % 3 === 0 && n % 5 === 0 && n % 7 === 0 && n % 9 === 0) {
            return n;
        }
    }
}

// convertir un nombre en tableau de chiffres
const getDigits = (number) => number.toString().split('').map(digit => parseInt(digit));

// encoder les chiffres
function getEncoding(digits) {
    let encoding = [];
    let dictionary = {};
    for (let i = 0; i < digits.length; i++) {
        let digit = digits[i];
        if (dictionary[digit] === undefined) {
        dictionary[digit] = i;
        encoding.push(`E${digit}`);
        } else {
        encoding.push(`R${dictionary[digit] + 1}`);
        }
    }
    return encoding;
}

// exécution
let number = findNumber();
let digits = getDigits(number);
let encoding = getEncoding(digits);

// affichage des résultats
console.log(`N = ${number}`);
console.log(`L = ${digits.join(', ')}`);
console.log(`L' = ${encoding.join(', ')}`);


