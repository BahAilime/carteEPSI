<script setup>
import Path from "@/components/Path.vue";
import { Graph, shortestPath } from 'graph-data-structure';
import data from "../spots.json";

/**
 * Converti une liste de noms de "spots" en liste de coordonnées
 * @param {string[]} spots - Liste de nom de spots
 * @returns {number[][]} - Liste de coordonées
 */
function spotsToCoordinates(spots) {
  const coordinates = [];
  for (let i = 0; i < spots.length; i++) {
    const spot = data.filter(coo => coo.name === spots[i])[0];
    coordinates.push([spot.x, spot.y]);
  }
  return coordinates;
}

let graph = new Graph()

function notDirectedGraph(graph, from, to, weight = 1) {
  graph.addEdge(from, to, weight);
  graph.addEdge(to, from, weight);
}

// Chaque salle a une salle dev qui corespond (dev=devant)
// il y a un noeud C109 et C101 ou sont relié toutes les salles des deux bouts du couloir


notDirectedGraph(graph, 'E0-G', 'dev009')
notDirectedGraph(graph, '002', 'dev002')
notDirectedGraph(graph, '003', 'dev003')
notDirectedGraph(graph, '007', 'dev007')
notDirectedGraph(graph, '008', 'dev008')
notDirectedGraph(graph, '009', 'dev009')
notDirectedGraph(graph, '011', 'dev011')
notDirectedGraph(graph, 'ENTREE', 'CACCUEIL')
notDirectedGraph(graph, 'CPEDAGO', 'CACCUEIL')
notDirectedGraph(graph, 'ACCUEIL', 'CACCUEIL')
notDirectedGraph(graph, 'CPEDAGO', 'PEDAGO')
notDirectedGraph(graph, 'CPEDAGO', 'C1')
notDirectedGraph(graph, 'C2', 'C1')
notDirectedGraph(graph, 'C2', 'C3')
notDirectedGraph(graph, 'dev001', 'C3')
notDirectedGraph(graph, 'dev001', 'C4')
notDirectedGraph(graph, 'dev002', 'C4')
notDirectedGraph(graph, 'dev003', 'C4')
notDirectedGraph(graph, 'dev003', 'C5')
notDirectedGraph(graph, 'C6', 'C5')
notDirectedGraph(graph, 'C6', 'CSUPCOM')
notDirectedGraph(graph, 'CSUPCOM', 'SUPCOM')
notDirectedGraph(graph, 'CSUPCOM', 'dev011')
notDirectedGraph(graph, 'dev007', 'dev011')
notDirectedGraph(graph, 'dev007', 'dev008')
notDirectedGraph(graph, 'dev009', 'dev008')
notDirectedGraph(graph, 'dev002', 'CCAFET')
notDirectedGraph(graph, 'E0-H', 'CCAFET')
notDirectedGraph(graph, 'E0-D', 'CAFET2')
notDirectedGraph(graph, 'CAFET1', 'CAFET2')
notDirectedGraph(graph, 'CAFET1', 'ACCUEIL')

notDirectedGraph(graph, 'E0-H', 'E1-H', 10)
notDirectedGraph(graph, 'E0-D', 'E1-D', 10)
notDirectedGraph(graph, 'E0-G', 'E1-G', 10)

notDirectedGraph(graph, '100', 'dev100')
notDirectedGraph(graph, '101', 'dev101')
notDirectedGraph(graph, 'dev100', 'dev101')

notDirectedGraph(graph, '102', 'dev102')
notDirectedGraph(graph, 'dev102', 'dev101')

notDirectedGraph(graph, '104', 'dev104')
notDirectedGraph(graph, 'dev102', 'dev104')
notDirectedGraph(graph, 'dev105', 'dev104')

notDirectedGraph(graph, '105', 'dev105')
notDirectedGraph(graph, '106', 'dev106')
notDirectedGraph(graph, 'dev105', 'dev106')

notDirectedGraph(graph, '107', 'dev107')
notDirectedGraph(graph, 'dev106', 'dev107')
notDirectedGraph(graph, '108', 'dev108')
notDirectedGraph(graph, 'dev107', 'dev108')
notDirectedGraph(graph, '109', 'dev109')
notDirectedGraph(graph, 'C109', 'E1-G')
notDirectedGraph(graph, 'C109', 'dev108')
notDirectedGraph(graph, 'C109', 'dev109')
notDirectedGraph(graph, 'C109', 'dev109B')
notDirectedGraph(graph, 'C109', 'dev110')
notDirectedGraph(graph, 'C109', 'dev111')
notDirectedGraph(graph, 'C109', 'dev112')

notDirectedGraph(graph, 'C101', 'dev101')
notDirectedGraph(graph, 'C101', 'dev102')
notDirectedGraph(graph, 'dev101', 'E1-D')
notDirectedGraph(graph, 'C101', 'C109')

notDirectedGraph(graph, '110', 'dev110')
notDirectedGraph(graph, '111', 'dev111')
notDirectedGraph(graph, 'dev110', 'dev111')

notDirectedGraph(graph, '112', 'dev112')
notDirectedGraph(graph, 'dev110', 'dev112')

notDirectedGraph(graph, '113', 'dev113')
notDirectedGraph(graph, 'dev106', 'dev113')
notDirectedGraph(graph, 'MYDIL', 'devMYDIL')
notDirectedGraph(graph, 'E1-H', 'devMYDIL')
notDirectedGraph(graph, 'C101', 'devMYDIL')

notDirectedGraph(graph, '200', 'devBOXD')
notDirectedGraph(graph, 'BOXA', 'devBOXA')
notDirectedGraph(graph, 'BOXB', 'devBOXB')
notDirectedGraph(graph, 'BOXC', 'devBOXC')
notDirectedGraph(graph, 'BOXD', 'devBOXD')
notDirectedGraph(graph, 'BOXE', 'devBOXE')
notDirectedGraph(graph, 'BOXF', 'devBOXF')
notDirectedGraph(graph, 'BOXG', 'devBOXG')
notDirectedGraph(graph, 'devBOXD', 'devBOXE')
notDirectedGraph(graph, 'devBOXC', 'devBOXE')
notDirectedGraph(graph, 'devBOXC', 'devBOXF')
notDirectedGraph(graph, 'devBOXB', 'devBOXF')
notDirectedGraph(graph, 'devBOXB', 'devBOXA')
notDirectedGraph(graph, 'devBOXG', 'devBOXA')
notDirectedGraph(graph, 'devBOXG', 'CE2-D')
notDirectedGraph(graph, 'E2-D', 'CE2-D')
notDirectedGraph(graph, 'E2-D', 'dev201')
notDirectedGraph(graph, 'C219', 'dev201')
notDirectedGraph(graph, 'C219', 'dev219')
notDirectedGraph(graph, 'C219', 'dev202')
notDirectedGraph(graph, 'dev203', 'dev202')
notDirectedGraph(graph, 'C202', 'dev202')
notDirectedGraph(graph, 'dev203', 'C202')
notDirectedGraph(graph, 'C202', 'dev218')
notDirectedGraph(graph, 'dev203', 'dev204')
notDirectedGraph(graph, 'dev205', 'dev204')
notDirectedGraph(graph, 'dev205', 'C207')
notDirectedGraph(graph, 'devMOOC', 'C207')
notDirectedGraph(graph, 'dev208', 'C207')
notDirectedGraph(graph, 'MOOC', 'devMOOC')
notDirectedGraph(graph, '212B', 'dev213')
notDirectedGraph(graph, 'devMOOC', 'dev213')
notDirectedGraph(graph, 'dev208', 'E2-G')
notDirectedGraph(graph, 'dev208', 'C209')
notDirectedGraph(graph, 'dev209', 'C209')
notDirectedGraph(graph, 'dev210', 'C209')
notDirectedGraph(graph, 'dev211', 'C209')
notDirectedGraph(graph, 'dev212', 'C209')

notDirectedGraph(graph, '201', 'dev201')
notDirectedGraph(graph, '202', 'dev202')
notDirectedGraph(graph, '203', 'dev203')
notDirectedGraph(graph, '204', 'dev204')
notDirectedGraph(graph, '205', 'dev205')

notDirectedGraph(graph, '207', 'dev207')
notDirectedGraph(graph, '208', 'dev208')
notDirectedGraph(graph, '209', 'dev209')
notDirectedGraph(graph, '209B', 'dev209B')
notDirectedGraph(graph, '210', 'dev210')
notDirectedGraph(graph, '211', 'dev211')
notDirectedGraph(graph, '212', 'dev212')
notDirectedGraph(graph, '213', 'dev213')
notDirectedGraph(graph, '218', 'dev218')
notDirectedGraph(graph, '219', 'dev219')
notDirectedGraph(graph, '221', 'dev221')

notDirectedGraph(graph, 'E1-G', 'E2-G', 15)
notDirectedGraph(graph, 'E1-D', 'E2-D', 15)

notDirectedGraph(graph, 'E0-G', 'E2-G', 10)
notDirectedGraph(graph, 'E0-D', 'E2-D', 10)

let way = spotsToCoordinates(shortestPath(graph,'CAFET1', '109').nodes);

const specialList0 = [];
const specialList1 = [];
const specialList2 = [];
const specialList3 = [];

const sortNodes = (nodes) => {
  const categories = {
    category0: [],
    category1: [],
    category2: [],
    category3: [],
    other: []
  };

  nodes.forEach(node => {
    if (node.startsWith('0') || node.startsWith('dev0') || node.startsWith('C0') || node.startsWith('E0') || specialList0.includes(node)) {
      categories.category0.push(node);
    } else if (node.startsWith('1') || node.startsWith('dev1') || node.startsWith('C1') || node.startsWith('E1') || specialList1.includes(node)) {
      categories.category1.push(node);
    } else if (node.startsWith('2') || node.startsWith('dev2') || node.startsWith('C2') || node.startsWith('E2') || node.startsWith('BOX') || node.startsWith('devBOX') || specialList2.includes(node)) {
      categories.category2.push(node);
    } else if (node.startsWith('3') || node.startsWith('dev3') || node.startsWith('C3') || node.startsWith('E3') || specialList3.includes(node)) {
      categories.category3.push(node);
    } else {
      categories.other.push(node)
    }
  });

  return categories;
};

const sortedNodes = sortNodes(shortestPath(graph,'002', '207').nodes);

console.log(sortedNodes);
</script>

<template>
  <div class="levels">
    <div class="level level--1" aria-label="Level 1">
      <h1 class="level__title">RDC: EPSI / ICL / IDRAC / IFAG / WIS</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category0)" />
      <img src="../../img/E1.png" alt="">
      <div class="level__pins">
        <a class="pin pin--1-1" data-category="1" data-space="1.01" href="#" aria-label="Pin for Apple Heart">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--appleheart"><use xlink:href="#icon-appleheart"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-2" data-category="1" data-space="1.02" href="#" aria-label="Pin for Crazy Banana">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--bananas"><use xlink:href="#icon-bananas"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-3" data-category="2" data-space="1.03" href="#" aria-label="Pin for Folding Life">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--origami"><use xlink:href="#icon-origami"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-4" data-category="3" data-space="1.04" href="#" aria-label="Pin for Dress me not">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--dress"><use xlink:href="#icon-dress"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-5" data-category="4" data-space="1.05" href="#" aria-label="Pin for Meditation Garden">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--tree2"><use xlink:href="#icon-tree2"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-6" data-category="1" data-space="1.06" href="#" aria-label="Pin for Seed of Life">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--avocado"><use xlink:href="#icon-avocado"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-7" data-category="1" data-space="1.07" href="#" aria-label="Pin for Raw Delight">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--cake"><use xlink:href="#icon-cake"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-8" data-category="1" data-space="1.08" href="#" aria-label="Pin for The Wizard">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--mushroom"><use xlink:href="#icon-mushroom"></use></svg>
									</span>
        </a>
        <a class="pin pin--1-9" data-category="1" data-space="1.09" href="#" aria-label="Pin for Smoothies &amp; Soul">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--pear"><use xlink:href="#icon-pear"></use></svg>
									</span>
        </a>
      </div>
      <!-- /level__pins -->
    </div>
    <div class="level level--2" aria-label="Level 2">
      <h1 class="level__title">Étage 1: ICL / IEFT / IFAG / IGEFI</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category1)" />
      <img src="../../img/E2.png" alt="">
      <div class="level__pins">
        <a class="pin pin--2-1" data-category="1" data-space="2.01" href="#" aria-label="Pin for Grilled Chipotle">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--pepper"><use xlink:href="#icon-pepper"></use></svg>
									</span>
        </a>
        <a class="pin pin--2-2" data-category="2" data-space="2.02" href="#" aria-label="Pin for Rocketship Tech">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--rocket"><use xlink:href="#icon-rocket"></use></svg>
									</span>
        </a>
        <a class="pin pin--2-3" data-category="2" data-space="2.03" href="#" aria-label="Pin for Which Bug?">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--bug"><use xlink:href="#icon-bug"></use></svg>
									</span>
        </a>
        <a class="pin pin--2-4" data-category="3" data-space="2.04" href="#" aria-label="Pin for Cognitio">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--books"><use xlink:href="#icon-books"></use></svg>
									</span>
        </a>
        <a class="pin pin--2-5" data-category="1" data-space="2.05" href="#" aria-label="Pin for The Eggplanthead">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--eggplant"><use xlink:href="#icon-eggplant"></use></svg>
									</span>
        </a>
        <a class="pin pin--2-6" data-category="1" data-space="2.06" href="#" aria-label="Pin for Superfood">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--strawberry"><use xlink:href="#icon-strawberry"></use></svg>
									</span>
        </a>
        <a class="pin pin--2-7" data-category="3" data-space="2.07" href="#" aria-label="Pin for No Princess">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--heart"><use xlink:href="#icon-heart"></use></svg>
									</span>
        </a>
        <a class="pin pin--2-8" data-category="3" data-space="2.08" href="#" aria-label="Pin for Tool Exchange">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--wrench"><use xlink:href="#icon-wrench"></use></svg>
									</span>
        </a>
      </div>
      <!-- /level__pins -->
    </div>
    <div class="level level--3" aria-label="Level 3">
      <h1 class="level__title">Étage 2: EPSI / WIS</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category2)" />
      <img src="../../img/E3.png" alt="">
      <div class="level__pins">
        <a class="pin pin--3-1" data-category="1" data-space="3.01" href="#" aria-label="Pin for Oolong House">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--tea"><use xlink:href="#icon-tea"></use></svg>
									</span>
        </a>
        <a class="pin pin--3-2" data-category="2" data-space="3.02" href="#" aria-label="Pin for Enlightend Path">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--pyramid"><use xlink:href="#icon-pyramid"></use></svg>
									</span>
        </a>
        <a class="pin pin--3-3" data-category="3" data-space="3.03" href="#" aria-label="Pin for What makes us walk">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--shoe"><use xlink:href="#icon-shoe"></use></svg>
									</span>
        </a>
        <a class="pin pin--3-4" data-category="3" data-space="3.04" href="#" aria-label="Pin for Your Last Shirt">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--shirt"><use xlink:href="#icon-shirt"></use></svg>
									</span>
        </a>
        <a class="pin pin--3-5" data-category="4" data-space="3.05" href="#" aria-label="Pin for Breathe">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--tree"><use xlink:href="#icon-tree"></use></svg>
									</span>
        </a>
        <a class="pin pin--3-6" data-category="4" data-space="3.06" href="#" aria-label="Pin for Feel the Grass">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--grass"><use xlink:href="#icon-grass"></use></svg>
									</span>
        </a>
        <a class="pin pin--3-7" data-category="4" data-space="3.07" href="#" aria-label="Pin for Star Gazer">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--star"><use xlink:href="#icon-star"></use></svg>
									</span>
        </a>
      </div>
      <!-- /level__pins -->
    </div>
    <div class="level level--4" aria-label="Level 4">
      <h1 class="level__title">Étage 3: IDRAC / IET / SUP DE COM</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category3)" />
      <img src="../../img/E4.png" alt="">
      <div class="level__pins">
        <a class="pin pin--4-1" data-category="1" data-space="4.01" href="#" aria-label="Pin for Cold Soup Kitchen">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--tomato"><use xlink:href="#icon-tomato"></use></svg>
									</span>
        </a>
        <a class="pin pin--4-2" data-category="2" data-space="4.02" href="#" aria-label="Pin for Docu Dome">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--cinema"><use xlink:href="#icon-cinema"></use></svg>
									</span>
        </a>
        <a class="pin pin--4-3" data-category="3" data-space="4.03" href="#" aria-label="Pin for Little Artist">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--paint-brush"><use xlink:href="#icon-paint-brush"></use></svg>
									</span>
        </a>
        <a class="pin pin--4-4" data-category="4" data-space="4.04" href="#" aria-label="Pin for Sacred Symmetry">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--modx"><use xlink:href="#icon-modx"></use></svg>
									</span>
        </a>
        <a class="pin pin--4-5" data-category="4" data-space="4.05" href="#" aria-label="Pin for Hot Tub Festival">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--droplet"><use xlink:href="#icon-droplet"></use></svg>
									</span>
        </a>
        <a class="pin pin--4-6" data-category="2" data-space="4.06" href="#" aria-label="Pin for Love 2 Cook">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--cupcake"><use xlink:href="#icon-cupcake"></use></svg>
									</span>
        </a>
        <a class="pin pin--4-7" data-category="2" data-space="4.07" href="#" aria-label="Pin for Permaculture Hub">
									<span class="pin__icon">
										<svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
										<svg class="icon icon--logo icon--leafcircle"><use xlink:href="#icon-leafcircle"></use></svg>
									</span>
        </a>
      </div>
      <!-- /level__pins -->
    </div>
  </div>
  <!-- /levels -->
</template>

<style scoped>

</style>