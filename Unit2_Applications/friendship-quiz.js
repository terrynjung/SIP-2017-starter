// questions to be randomly asked on page load
var questionsList = ["What are your/your friend's favorite foods?", "What are your/your friend's favorite animals?"];


//randomly chooses a question to display
function init() {
  var randomIndex = Math.floor(Math.random() * questionsList.length);
  document.getElementById("question").innerHTML = questionsList[randomIndex];
}

window.onload = init;

var answerList = []; //initialize answerList to be empty

//adds user-submitted answer to answerList
function submitAnswer() {
  var answer = document.getElementById("answerInput").value;
  var answer2 = answer.toUpperCase();
  document.getElementById("answerInput").value = "";
  answerList.push(answer2);
}

//prints out results of the friendship-quiz
function displayMessage(message){
  document.getElementById("result").innerHTML = message;
}

//checks if user-submitted guess is in answerList
function checkGuess() {
  var guess = document.getElementById("guessInput").value;
  var guess2 = guess.toUpperCase();
  if (answerList.indexOf(guess2) == -1){
    displayMessage("Not even friends... Try again!");
  }
  else{
    displayMessage("BEST FRIENDS!!");
  }
}
