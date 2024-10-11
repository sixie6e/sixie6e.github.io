document.addEventListener('DOMContentLoaded', () => {
  nextButton.classList.add('hide');
});

const beginButton = document.getElementById('begin');
const nextButton = document.getElementById('next');
const nextSetButton = document.getElementById('next-set')
const mushroomContainerElement = document.getElementById('mushroom-container');
const mushroomElement = document.getElementById('mushroom');
const answerButtonsElement = document.getElementById('answer-buttons');
const resultsElement = document.getElementById('results');
const mushroomButton = document.getElementById('mushroom-btn');
const lichenButton = document.getElementById('lichen-btn');

const mhs = new Image(200,200);
mhs.src = 'img/manyheadedslime.jpg';
const bsl = new Image(200,200);
bsl.src = 'img/britishsoldierlichen.png';
const waspmold = new Image(200,200);
waspmold.src = 'img/bgwaspmold0.png';
const ppc = new Image(200,200);
ppc.src = 'img/ppc.png';
const ls = new Image(200,200);
ls.src = 'img/lessersulphur.png';
const graylegs = new Image(200,200);
graylegs.src = 'img/graylegs.png';
const rfpc = new Image(200,200);
rfpc.src = 'img/rfpc.png';
const thorn = new Image(200,200);
thorn.src = 'img/thorn.png';
const sd = new Image(200,200);
sd.src = 'img/sulphurdust.png';
const ladder = new Image(200,200);
ladder.src = 'img/ladder.png';
const pretzel = new Image(200,200);
pretzel.src = 'img/pretzel.png';
const hc = new Image(200,200);
hc.src = 'img/honeycomb.png';
const swarmingspine = new Image(200,200);
swarmingspine.src = 'img/swarmingspine.png';
const turban = new Image(200,200);
turban.src = 'img/turban.png';
const pel = new Image(200,200);
pel.src = 'img/pinkearth.png';
const lp = new Image(200,200);
lp.src = 'img/lipstick.png';
const vfl = new Image(200,200);
vfl.src = 'img/variegatedfoam.png';
const tsol = new Image(200,200);
tsol.src = 'img/tsol.png';
const branchedpc = new Image(200,200);
branchedpc.src = 'img/branchedpc.png';
const odisco = new Image(200,200);
odisco.src = 'img/odisco.png';
const firedot = new Image(200,200);
firedot.src = 'img/firedot.png';
const lung = new Image(200,200);
lung.src = 'img/lungwort.png';
const dragonhorn = new Image(200,200);
dragonhorn.src = 'img/dragonhorn.png';
const reindeer = new Image(200,200);
reindeer.src = 'img/reindeer.png';
const cylpow = new Image(200,200);
cylpow.src = 'img/cylpow.png';


const enada = new Image(200,200);
enada.src = 'img/enada.png';
const cl = new Image(200,200);
cl.src = 'img/chickenlips.png';
const so = new Image(200,200);
so.src = 'img/smokedoysterling.png';
const ge = new Image(200,200);
ge.src = 'img/goldenear.png';
const chrom = new Image(200,200);
chrom.src = 'img/chromosera.png';
const ahm = new Image(200,200);
ahm.src = 'img/ahm.png';
const reddock = new Image(200,200);
reddock.src = 'img/reddock.png';
const dryad = new Image(200,200);
dryad.src = 'img/dryad.png';
const lb = new Image(200,200);
lb.src = 'img/laqbracket.png';
const vpspore = new Image(200,200);
vpspore.src = 'img/violetpolyspore.png';
const hoyster = new Image(200,200);
hoyster.src = 'img/hairyoyster.png';
const vermwaxcap = new Image(200,200);
vermwaxcap.src = 'img/vermillion.png';
const cbf = new Image(200,200);
cbf.src = 'img/cbf.png';
const cparchment = new Image(200,200);
cparchment.src = 'img/parchment.png';
const tenuipes = new Image(200,200);
tenuipes.src = 'img/tenuipes.png';
const greenwood = new Image(200,200);
greenwood.src = 'img/greenwood.png';
const mycena = new Image(200,200);
mycena.src = 'img/mycena.png';
const wcoral = new Image(200,200);
wcoral.src = 'img/wcoral.png';
const yfc = new Image(200,200);
yfc.src = 'img/yfc.png';
const panellus = new Image(200,200);
panellus.src = 'img/panellus.png';
const gfmould = new Image(200,200);
gfmould.src = 'img/gfmould.png';
const mpball = new Image(200,200);
mpball.src = 'img/mpball.png';
const et = new Image(200,200);
et.src = 'img/earthtongue.png';
const ttail = new Image(200,200);
ttail.src = 'img/ttail.png';
const tubelet = new Image(200,200);
tubelet.src = 'img/tubelet.png';

images = [mhs, bsl, waspmold, ppc, ls, graylegs, rfpc, thorn, sd, ladder, pretzel, hc, swarmingspine, turban, pel, lp, vfl, tsol, branchedpc, odisco, firedot, lung, dragonhorn, reindeer, cylpow];
images1 = [enada, cl, so, ge, chrom, ahm, reddock, dryad, lb, vpspore, hoyster, vermwaxcap, tenuipes, wcoral, cbf, cparchment, mycena, greenwood, yfc, panellus, gfmould, mpball, et, ttail, tubelet];

const lichen = [
	{
		mushroom: images[0],
		answers: [ 
			{ text: 'Many-Headed Slime', correct: true },
			{ text: 'Brain Map Fungus', correct: false },
			{ text: 'Bolete', correct: false },
			{ text: 'Chanterelle', correct: false },
		]
	},
	{
		mushroom: images[1],
		answers: [
			{ text: 'Lipstick Powderhorn', correct: false },
			{ text: 'Red Fruited Pixie Cup', correct: false },
			{ text: 'British Soldier Lichen', correct: true },
			{ text: 'Powdered Funnel Lichen', correct: false },
		]
	},
	{
		mushroom: images[2],
		answers: [ 
			{ text: 'Bulbasauritae', correct: false },
			{ text: 'Wasp Nest Slime Mold', correct: true },
			{ text: 'Red Monster Fungus', correct: false },
			{ text: 'Spring-Ups', correct: false },
		]
	},
	{
		mushroom: images[3],
		answers: [ 
			{ text: 'Pebbled Pixie Cup', correct: true },
			{ text: 'Flaked Laurel', correct: false },
			{ text: 'Glistening Dew Cup', correct: false },
			{ text: 'Jack-in-the-Pulpit', correct: false },
		]
	},
	{
		mushroom: images[4],
		answers: [ 
			{ text: 'Lesser Sulphur Cup', correct: true },
			{ text: 'Cup of Sulphur', correct: false },
			{ text: 'Sulphur Sprouts', correct: false },
			{ text: 'Lesser Sulphur Shoots', correct: false },
		]
	},
	{
		mushroom: images[5],
		answers: [
			{ text: 'Lesser Gray Legs', correct: true },
			{ text: 'Wig of Grandmother', correct: false },
			{ text: 'Gray Shorts', correct: false },
			{ text: 'Lesser Gray Shorts', correct: false },
		]
	},	
	{
		mushroom: images[6],
		answers: [
			{ text: 'Cherry Turban', correct: false },
			{ text: 'Strawberry Pixie Cup', correct: false },
			{ text: 'Red-Fruited Pixie Cup', correct: true },
			{ text: 'Strawberry Turban', correct: false },
		]
	},
	{
		mushroom: images[7],
		answers: [ 
			{ text: 'Thorn Lichen', correct: true },
			{ text: 'Horn Lichen', correct: false },
			{ text: 'Pointed Lichen', correct: false },
			{ text: 'Sharp Lichen', correct: false },
		]
	},
	{
		mushroom: images[8],
		answers: [ 
			{ text: 'Penicillin', correct: false },
			{ text: 'Tree Mold Lichen', correct: false },
			{ text: 'Sulphur Dust Lichen', correct: true },
			{ text: 'Green Foam Lichen', correct: false },
		]
	},
	{
		mushroom: images[9],
		answers: [ 
			{ text: 'Ladder Lichen', correct: true },
			{ text: 'False Stories Lichen', correct: false },
			{ text: 'Skyscraper Lichen', correct: false },
			{ text: 'Extension Lichen', correct: false },
		]
	},
	{
		mushroom: images[10],
		answers: [
			{ text: 'Pretzel Fungus', correct: false },
			{ text: 'Seafoam Slime Mold', correct: false },
			{ text: 'Yellow Tube Fungus', correct: false },
			{ text: 'Pretzel Slime Mold', correct: true },
		]
	},
	{
		mushroom: images[11],
		answers: [ 
			{ text: 'Mermaid Armpit', correct: false },
			{ text: 'Angel Hair Slime Mold', correct: false },
			{ text: 'Honeycomb Coral Slime Mold', correct: true },
			{ text: 'Angel Hair Fungus', correct: false },
		]
	},
	{
		mushroom: images[12],
		answers: [
			{ text: 'Spine Teeth', correct: false },
			{ text: 'Butt Teeth', correct: false },
			{ text: 'Swarming Spine', correct: true },
			{ text: 'Swarming Butt', correct: false },
		]
	},
	{
		mushroom: images[13],
		answers: [
			{ text: 'Alveoli', correct: false },
			{ text: 'Salamander Trees', correct: false },
			{ text: 'Turban Cup Lichen', correct: true },
			{ text: 'Alveoli Cup Lichen', correct: false },
		]
	},
	{
		mushroom: images[14],
		answers: [ 
			{ text: 'Pink Earth Lichen', correct: true },
			{ text: 'Mermaid Armpit', correct: false },
			{ text: 'Pink Jheri Lichen', correct: false },
			{ text: 'Jheri Lichen', correct: false },
		]
	},
	{
		mushroom: images[15],
		answers: [
			{ text: 'Powdered Lipstick', correct: false },
			{ text: 'Cladonia Simplex', correct: false },
			{ text: 'Complex Cladonia', correct: false },
			{ text: 'Lipstick Powderhorn', correct: true },
		]
	},
	{
		mushroom: images[16],
		answers: [ 
			{ text: 'Variegated Foam Lichen', correct: true },
			{ text: 'Dog Vomit Slime Mold', correct: false },
			{ text: 'Foam Vomit Lichen', correct: false },
			{ text: 'Variegated Cluster Fungus', correct: false },
		]
	},
	{
		mushroom: images[17],
		answers: [
			{ text: 'Toy Soldiers', correct: true },
			{ text: 'Astin`s Lichen', correct: false },
			{ text: 'Wheaton`s Lichen', correct: false },
			{ text: 'Gossett`s Lichen', correct: false },
		]
	},
	{
		mushroom: images[18],
		answers: [
			{ text: 'Powdered Hands', correct: false },
			{ text: 'Powdered Arms', correct: false },
			{ text: 'Branched Pixie Cup', correct: true },
			{ text: 'Cartridge Bundle', correct: false },
		]
	},
	{
		mushroom: images[19],
		answers: [
			{ text: 'Panic Around the Disco', correct: false },
			{ text: 'Panic At the Orange', correct: false },
			{ text: 'Orange Round', correct: false },
			{ text: 'Orange Disco', correct: true },
		]
	},
	{
		mushroom: images[20],
		answers: [ 
			{ text: 'Rim Lichen', correct: false },
			{ text: 'Brown Eye Lichen', correct: false },
			{ text: 'Sulphur Firedot', correct: true },
			{ text: 'Brown Eye Firedot', correct: false },
		]
	},
	{
		mushroom: images[21],
		answers: [
			{ text: 'Tree Cabbagewort', correct: false },
			{ text: 'Lung Cabbagewort', correct: false },
			{ text: 'Tree Lungwort', correct: true },
			{ text: 'Placenta Treewort', correct: false },
		]
	},
	{
		mushroom: images[22],
		answers: [ 
			{ text: 'Cannabis Lichen', correct: false },
			{ text: 'Bud Rot Lichen', correct: false },
			{ text: 'Dragon Horn', correct: true },
			{ text: 'Dragon Teeth', correct: false },
		]
	},
	{
		mushroom: images[23],
		answers: [ 
			{ text: 'Reindeer Lichen', correct: true },
			{ text: 'Antler Shrub', correct: false },
			{ text: 'Bramble Lichen', correct: false },
			{ text: 'Thorn Lichen', correct: false },
		]
	},
	{
		mushroom: images[24],
		answers: [ 
			{ text: 'Cylindrical Powderhorn', correct: true },
			{ text: 'Sulphur Stalks', correct: false },
			{ text: 'Sulphur Powderhorn', correct: false },
			{ text: 'Common Powder Stalks', correct: false },
		]
	},
]
	
const mushrooms = [	

	{
		mushroom: images1[0],
		answers: [
			{ text: 'Widow Brew', correct: false },
			{ text: 'White Amanita', correct: false },
			{ text: 'Eastern NorAm Destroying Angel', correct: true },
			{ text: 'Powder Top', correct: false },
		]
	},
		{
		mushroom: images1[1],
		answers: [
			{ text: 'Osprey Farts', correct: false },
			{ text: 'Hen Pecks', correct: false },
			{ text: 'Rooster Fingers', correct: false },
			{ text: 'Chicken Lips', correct: true },
		]
	},
		{
		mushroom: images1[2],
		answers: [ 
			{ text: 'Puff Balls', correct: false },
			{ text: 'Smoked Oysterling', correct: true },
			{ text: 'Bolete', correct: false },
			{ text: 'Wood Acne', correct: false },
		]
	},
	{
		mushroom: images1[3],
		answers: [
			{ text: 'Forest Jelly', correct: false },
			{ text: 'Jelly Lichen', correct: false },
			{ text: 'Golden Ear', correct: true },
			{ text: 'Jelly Ear', correct: false },
		]
	},
	{
		mushroom: images1[4],
		answers: [ 
			{ text: 'Brown Buttons', correct: false },
			{ text: 'Hyalorbilia', correct: false },
			{ text: 'Golden Amanita', correct: false },
			{ text: 'Chromosera', correct: true },
		]
	},
		{
		mushroom: images1[5],
		answers: [ 
			{ text: 'Smooth Haircap Moss', correct: false },
			{ text: 'Smooth Algal Cap', correct: false },
			{ text: 'Green Shower Cap', correct: false },
			{ text: 'Algal Haircap Moss', correct: true },
		]
	},
	{
		mushroom: images1[6],
		answers: [
			{ text: 'Red Spot', correct: false },
			{ text: 'Aged Red Fungus', correct: false },
			{ text: 'Aged Wine Rash', correct: false },
			{ text: 'Red Dock Spot', correct: true },
		]
	},
	{
		mushroom: images1[7],
		answers: [
			{ text: 'Druid Bracket', correct: false },
			{ text: 'Pancake Bracket', correct: false },
			{ text: 'Dryad`s Saddle', correct: true },
			{ text: 'Druid`s Saddle', correct: false },
		]
	},
		{
		mushroom: images1[8],
		answers: [ 
			{ text: 'Lacquered Bracket', correct: true },
			{ text: 'Shiny Stump Ladder', correct: false },
			{ text: 'Shiny Stump Step', correct: false },
			{ text: 'Lacquered Stump Step', correct: false },
		]
	},
	{
		mushroom: images1[9],
		answers: [
			{ text: 'Violet Polyspore', correct: true },
			{ text: 'Thrown Paint Lichen', correct: false },
			{ text: 'Thrown Paint Polyspore', correct: false },
			{ text: 'Violet Paint Lichen', correct: false },
		]
	},	
	{
		mushroom: images1[10],
		answers: [ 
			{ text: 'Ear of Grandpa', correct: false },
			{ text: 'Hairy Ear of Grandpa', correct: false },
			{ text: 'Hairy Oyster', correct: true },
			{ text: 'Oyster of Grandpa', correct: false },
		]
	},
	{
		mushroom: images1[11],
		answers: [
			{ text: 'Fluorescent Forest Cap', correct: false },
			{ text: 'Cascading Waxcap', correct: false },
			{ text: 'Vermillion Waxcap', correct: true },
			{ text: 'Fluorescent Cascading Waxcap', correct: false },
		]
	},
	{
		mushroom: images1[12],
		answers: [
			{ text: 'Christmas Stalk', correct: false },
			{ text: 'Moth Antlers', correct: false },
			{ text: 'Snowy Reindeer', correct: false },
			{ text: 'Cordyceps Tenuipes', correct: true },
		]
	},
	{
		mushroom: images1[13],
		answers: [ 
			{ text: 'White Coral Fungus', correct: true },
			{ text: 'Terrestrial Coral', correct: false },
			{ text: 'Earth Coral Fungus', correct: false },
			{ text: 'Land Coral Fungus', correct: false },
		]
	},
	{
		mushroom: images1[14],
		answers: [
			{ text: 'Grandpa`s Mole', correct: false },
			{ text: 'Grandma`s Growth', correct: false },
			{ text: 'Crystal Brain', correct: true },
			{ text: 'Brain Jelly', correct: false },
		]
	},
	{
		mushroom: images1[15],
		answers: [
			{ text: 'Candy Corn Lichen', correct: false },
			{ text: 'Halloween Lichen', correct: false },
			{ text: 'Crowded Parchment', correct: true },
			{ text: 'Clownfish Teeth', correct: false },
		]
	},
		{
		mushroom: images1[16],
		answers: [
			{ text: 'Cradle Fungus', correct: false },
			{ text: 'Ribcage Mushroom', correct: false },
			{ text: 'Stump Creeper', correct: false },
			{ text: 'Snowbank Fairy Helmet', correct: true },
		]
	},
	{
		mushroom: images1[17],
		answers: [
			{ text: 'Greenwood`s Cup', correct: false },
			{ text: 'Green Wood Bracket', correct: false },
			{ text: 'Green Wood Cup', correct: true },
			{ text: 'Blue Impetigo', correct: false },
		]
	},
	{
		mushroom: images1[18],
		answers: [
			{ text: 'Yellow Fairy Cups', correct: true },
			{ text: 'Yellow Jelly Dots', correct: false },
			{ text: 'Fairy Jelly Dots', correct: false },
			{ text: 'Fairy Jelly Cups', correct: false },
		]
	},	
	{
		mushroom: images1[19],
		answers: [
			{ text: 'Frog Steps', correct: false },
			{ text: 'Fairy Steps', correct: false },
			{ text: 'Luminescent Panellus', correct: true },
			{ text: 'Lumipani', correct: false },
		]
	},
	{
		mushroom: images1[20],
		answers: [
			{ text: 'Hairy Froots', correct: false },
			{ text: 'Shudathrohnitout', correct: false },
			{ text: 'Tired Froots', correct: false },
			{ text: 'Grey Fruit Mold', correct: true },
		]
	},
	{
		mushroom: images1[21],
		answers: [
			{ text: 'Marshmallow Ball', correct: false },
			{ text: 'Marshmallow Puff', correct: false },
			{ text: 'Meadow Puff Ball', correct: true },
			{ text: 'Meadow Marshmallow', correct: false },
		]
	},
	{
		mushroom: images1[22],
		answers: [
			{ text: 'Orange Tree Tongue', correct: false },
			{ text: 'Orange Wind Socks', correct: false },
			{ text: 'Irregular Earth Tongue', correct: true },
			{ text: 'Orange Earth Socks', correct: false },
		]
	},
	{
		mushroom: images1[23],
		answers: [
			{ text: 'Cascading Turkey', correct: false },
			{ text: 'Tiled Turkey', correct: false },
			{ text: 'Layered Turkey', correct: false },
			{ text: 'Turkey Tail', correct: true },
		]
	},
	{
		mushroom: images1[24],
		answers: [ 
			{ text: 'Wood Acne', correct: false },
			{ text: 'Angel Anemone', correct: false },
			{ text: 'White Tubelet', correct: true },
			{ text: 'Angel Tubelet', correct: false },
		]
	},
]

let shuffledMushrooms;
let currentMushroomIndex;
let shuffledLichen;
let currentLichenIndex;
let score = 0;
mushroomButton.classList.add('hide');
lichenButton.classList.add('hide');
beginButton.addEventListener('click', choice);
nextSetButton.addEventListener('click', choice);
nextSetButton.classList.add('hide');

function choice() {
  beginButton.classList.add('hide');
  mushroomButton.classList.remove('hide');
  lichenButton.classList.remove('hide');
  mushroomButton.addEventListener('click', beginMycoMem);
  lichenButton.addEventListener('click', beginLichoMem);
}

function beginMycoMem() {
  mushroomButton.classList.add('hide');
  lichenButton.classList.add('hide'); 
  shuffledMushrooms = mushrooms.sort(() => Math.random() - .5);
  currentMushroomIndex = 0;
  mushroomContainerElement.classList.remove('hide');
  setNextMushroom();
}

function beginLichoMem() {
  mushroomButton.classList.add('hide');
  lichenButton.classList.add('hide');
  shuffledMushrooms = lichen.sort(() => Math.random() - .5);
  currentMushroomIndex = 0;
  mushroomContainerElement.classList.remove('hide');
  setNextMushroom();
}

function showMushroom(mushroom) {
  mushroomElement.innerHTML = "<img src=" + mushroom.mushroom.src + " />";
  mushroom.answers.forEach(answer => {
      const button = document.createElement('button');
      button.innerText = answer.text;
      button.classList.add('btn');
      if (answer.correct) {
          button.dataset.correct = answer.correct;
      }
      button.addEventListener('click', () => selectAnswer(button));
      answerButtonsElement.appendChild(button);
  });
}

function setStatusClass(element, correct) {
  clearStatusClass(element);
  if (correct) {
      element.classList.add('correct');
  } else {
      element.classList.add('incorrect');
  }
}

function clearStatusClass(element) {
  element.classList.remove('correct');
  element.classList.remove('incorrect');
}
nextButton.addEventListener('click', () => {
  currentMushroomIndex++;
  setNextMushroom();
});

function setNextMushroom() {
  resetState();
  showMushroom(shuffledMushrooms[currentMushroomIndex]);
}

function resetState() {
  clearStatusClass(document.body);
  //nextButton.classList.add('hide');
  while (answerButtonsElement.firstChild) {
      answerButtonsElement.removeChild(answerButtonsElement.firstChild);
  }
}

function selectAnswer(selectedButton) {
  Array.from(answerButtonsElement.children).forEach(button => {
      button.disabled = true;
      setStatusClass(button, button.dataset.correct);
  });

  const correct = selectedButton.dataset.correct;
  if (correct) {
      score++;
  }
  setStatusClass(selectedButton, correct);

  setTimeout(() => {
      if (shuffledMushrooms.length > currentMushroomIndex + 1) {
          nextButton.classList.remove('hide');
      } else {
          pauseMycoMem();
      }
      if (shuffledLichen.length > currentLichenIndex + 1) {
          nextButton.classList.remove('hide');
      } else {
          pauseMycoMem();
      }
  }, 50);
 
}

function setStatusClass(element, correct) {
  clearStatusClass(element);
  if (correct) {
      element.classList.add('correct');
  } else {
      element.classList.add('incorrect');
  }
}

function clearStatusClass(element) {
  element.classList.remove('correct');
  element.classList.remove('incorrect');
}

function pauseMycoMem() {
  mushroomContainerElement.classList.add('hide');
  nextButton.classList.add('hide');
  resultsElement.classList.remove('hide');
  resultsElement.innerHTML = `
      <h2><font color="ffffff"><center>Accuracy: ${score} out of ${shuffledMushrooms.length}</p></center></h2>
      <center><button onclick="restartMycoMem()">Restart</button> or you can go to the <button onclick="setTwo()">Next Set</button></center> or you can <button onclick="window.close()">Exit</button></center>`;
}

function restartMycoMem() {
  resultsElement.classList.add('hide');
  score = 0;
  currentMushroomIndex = 0;
  choice();
}
