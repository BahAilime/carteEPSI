<script setup>
import Path from "@/components/Path.vue";
import { Graph, shortestPath } from 'graph-data-structure';
import data from "../spots.json";
import levelData from "../descriptionData.json";

const level1Pins = levelData[0]["level0"];
const level2Pins = levelData[0]["level1"];
const level3Pins = levelData[0]["level2"];
const level4Pins = levelData[0]["level3"];

let source = "002";
let destination = "204";

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

notDirectedGraph(graph, 'dev209B', 'dev209')
notDirectedGraph(graph, 'dev221', 'dev219')
notDirectedGraph(graph, 'dev207', 'C207')

notDirectedGraph(graph, '325', 'dev317')
notDirectedGraph(graph, '317', 'dev317')
notDirectedGraph(graph, 'dev316', 'dev317')
notDirectedGraph(graph, 'dev316', '316')
notDirectedGraph(graph, 'dev316', 'dev315')
notDirectedGraph(graph, 'dev315', '315')
notDirectedGraph(graph, 'dev315', 'C314')
notDirectedGraph(graph, 'dev313', 'C314')
notDirectedGraph(graph, 'dev314', '314')
notDirectedGraph(graph, 'dev313', 'dev314')
notDirectedGraph(graph, 'dev313', '313')
notDirectedGraph(graph, 'dev313', 'dev312')
notDirectedGraph(graph, '312', 'dev312')
notDirectedGraph(graph, 'C312', 'dev312')
notDirectedGraph(graph, '311', 'dev311')
notDirectedGraph(graph, 'C312', 'dev311')
notDirectedGraph(graph, 'C312', 'devE3-G')
notDirectedGraph(graph, 'E3-G', 'devE3-G')
notDirectedGraph(graph, 'E3-G', 'E2-G', 10)
notDirectedGraph(graph, 'E3-G', 'E1-G', 15)
notDirectedGraph(graph, 'E3-G', 'E0-G', 25)
notDirectedGraph(graph, 'dev309', 'devE3-G')

notDirectedGraph(graph, 'dev309', '309')
notDirectedGraph(graph, 'dev309', 'dev308')
notDirectedGraph(graph, '308', 'dev308')
notDirectedGraph(graph, 'dev307', 'dev308')
notDirectedGraph(graph, 'dev307', '307')
notDirectedGraph(graph, 'dev307', 'dev306')
notDirectedGraph(graph, '306', 'dev306')
notDirectedGraph(graph, 'dev305', 'dev306')
notDirectedGraph(graph, 'dev305', '305')
notDirectedGraph(graph, 'dev305', 'dev304')
notDirectedGraph(graph, '304', 'dev304')
notDirectedGraph(graph, 'dev303', 'dev304')
notDirectedGraph(graph, 'dev303', '303')
notDirectedGraph(graph, '302', 'dev302')
notDirectedGraph(graph, 'dev303', 'dev302')
notDirectedGraph(graph, 'dev326', 'dev302')
notDirectedGraph(graph, 'dev326', '326')
notDirectedGraph(graph, 'dev326', '327')
notDirectedGraph(graph, 'dev326', 'CE3-D')
notDirectedGraph(graph, 'E3-D', 'CE3-D')
notDirectedGraph(graph, 'E3-D', 'E2-D', 10)
notDirectedGraph(graph, 'E3-D', 'E1-D', 15)
notDirectedGraph(graph, 'E3-D', 'E0-D', 25)
notDirectedGraph(graph, 'C300', 'CE3-D')
notDirectedGraph(graph, 'C300', '300')
notDirectedGraph(graph, '300', '3BOXA')
notDirectedGraph(graph, '300', '3BOXB')
notDirectedGraph(graph, '300', '3BOXC')
notDirectedGraph(graph, '300', '3BOXD')
notDirectedGraph(graph, '300', '3BOXE')
notDirectedGraph(graph, '300', '3BOXF')
notDirectedGraph(graph, '300', '3BOXG')
notDirectedGraph(graph, '300', '3BOXH')

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

const sortedNodes = sortNodes(shortestPath(graph, source, destination).nodes);

</script>

<template>

  <div class="levels">
    <div class="level level--1" aria-label="Level 1">
      <h1 class="level__title">RDC: EPSI / ICL / IDRAC / IFAG / WIS</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category0)" />
      <img src="../../img/E1.png" alt="">
      <div class="level__pins">
        <a
            v-for="(pin, index) in level1Pins"
            :key="index"
            class="pin"
            :class="'pin--1-' + (index + 1)"
            :data-category="pin.category"
            :data-space="pin.space"
            href="#"
            :aria-label="pin.label"
        >
          <span class="pin__icon">
            <svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
            <svg class="icon icon--logo" :class="'icon--' + pin.icon"><use :xlink:href="'#icon-' + pin.icon"></use></svg>
          </span>
        </a>
      </div>
    </div>
    <div class="level level--2" aria-label="Level 2">
      <h1 class="level__title">Étage 1: ICL / IEFT / IFAG / IGEFI</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category1)" />
      <img src="../../img/E2.png" alt="">
      <div class="level__pins">
        <a
            v-for="(pin, index) in level2Pins"
            :key="index"
            class="pin"
            :class="'pin--2-' + (index + 1)"
            :data-category="pin.category"
            :data-space="pin.space"
            href="#"
            :aria-label="pin.label"
        >
          <span class="pin__icon">
            <svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
            <svg class="icon icon--logo" :class="'icon--' + pin.icon"><use :xlink:href="'#icon-' + pin.icon"></use></svg>
          </span>
        </a>
      </div>
    </div>
    <div class="level level--3" aria-label="Level 3">
      <h1 class="level__title">Étage 2: ICL / IEFT / IFAG / IGEFI</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category2)" />
      <img src="../../img/E3.png" alt="">
      <div class="level__pins">
        <a
            v-for="(pin, index) in level3Pins"
            :key="index"
            class="pin"
            :class="'pin--3-' + (index + 1)"
            :data-category="pin.category"
            :data-space="pin.space"
            href="#"
            :aria-label="pin.label"
        >
          <span class="pin__icon">
            <svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
            <svg class="icon icon--logo" :class="'icon--' + pin.icon"><use :xlink:href="'#icon-' + pin.icon"></use></svg>
          </span>
        </a>
      </div>
    </div>
    <div class="level level--4" aria-label="Level 4">
      <h1 class="level__title">Étage 3: ICL / IEFT / IFAG / IGEFI</h1>
      <Path :coordinates="spotsToCoordinates(sortedNodes.category3)" />
      <img src="../../img/E4.png" alt="">
      <div class="level__pins">
        <a
            v-for="(pin, index) in level4Pins"
            :key="index"
            class="pin"
            :class="'pin--4-' + (index + 1)"
            :data-category="pin.category"
            :data-space="pin.space"
            href="#"
            :aria-label="pin.label"
        >
          <span class="pin__icon">
            <svg class="icon icon--pin"><use xlink:href="#icon-pin"></use></svg>
            <svg class="icon icon--logo" :class="'icon--' + pin.icon"><use :xlink:href="'#icon-' + pin.icon"></use></svg>
          </span>
        </a>
      </div>
    </div>
  </div>
  <!-- /levels -->

</template>

<style scoped>

</style>