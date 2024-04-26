var decisionTree = [
    {
        question: 'AB projemiz ile ilgili bilgi alabileceğiniz karar ağıcına hoş geldiniz',
        answers: [
            { text: 'Projenin hakkında bilgiler', followUp: 3 }, // 1. soruya geçiş
            { text: 'Uygulama Hakkında bilgiler', followUp: 2 } // 2. soruya geçiş
        ]
    },
    {
        question: '2. Soru: Ne düşünüyorsunuz?',
        answers: [
            { text: 'İyi', followUp: 3 }, // 3. soruya geçiş
            { text: 'Kötü', followUp: 4 } // 4. soruya geçiş
        ]
    },
    {
        question: '3. Soru: Başka bir şey söylemek ister misiniz?',
        answers: [
            { text: 'Evet', followUp: 5 }, // 5. soruya geçiş
            { text: 'Hayır', followUp: 6 } // 6. soruya geçiş
        ]
    },
    {
        question: '4. Soru: Neden kötü hissediyorsunuz?',
        answers: [
            { text: 'İşle ilgili', followUp: 7 }, // 7. soruya geçiş
            { text: 'Kişisel', followUp: 8 } // 8. soruya geçiş
        ]
    },
    {
        question: '5. Soru: Söylemek istediğiniz başka bir şey var mı?',
        answers: [
            { text: 'Evet', followUp: 9 }, // 9. soruya geçiş
            { text: 'Hayır', followUp: 10 } // 10. soruya geçiş
        ]
    },
    {
        question: '5. Soru: Söylemek istediğiniz başka bir şey var mı?',
        answers: [
            { text: 'Evet', followUp: 11 }, // 9. soruya geçiş
            { text: 'Hayır', followUp: 8 } // 10. soruya geçiş
        ]
    },

];

var currentQuestionIndex = 0;

function displayQuestion() {
    var questionContainer = document.getElementById('question-container');
    var questionElement = document.getElementById('question');
    var buttonContainer = document.getElementById('button-container');

    var currentQuestion = decisionTree[currentQuestionIndex];

    questionElement.textContent = currentQuestion.question;

    buttonContainer.innerHTML = ''; // Butonları temizle

    currentQuestion.answers.forEach(function (answer) {
        var button = document.createElement('button');
        button.textContent = answer.text;
        button.addEventListener('click', function () {
            handleAnswer(answer);
        });
        buttonContainer.appendChild(button);
    });
}

function handleAnswer(answer) {
    // Seçilen cevaba göre bir sonraki soruya geçiş
    currentQuestionIndex = answer.followUp;

    // Sorular bitene kadar devam et
    if (currentQuestionIndex < decisionTree.length) {
        displayQuestion();
    } else {
        alert('Karar ağacı tamamlandı!');
    }
}

// İlk soruyu görüntüle
displayQuestion();
