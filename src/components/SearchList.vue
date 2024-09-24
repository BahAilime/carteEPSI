<template>
  <aside class="spaces-list" id="spaces-list">
    <div class="search">
      <input class="search__input" placeholder="Search..." />
      <button class="boxbutton boxbutton--darker close-search" aria-label="Close details">
        <svg class="icon icon--cross">
          <use xlink:href="#icon-cross"></use>
        </svg>
      </button>
    </div>
    <span class="label">
      <input id="sort-by-name" class="label__checkbox" type="checkbox" aria-label="Show alphabetically"/>
      <label class="label__text">A - Z</label>
    </span>
    <ul class="list grouped-by-category">
      <li
          v-for="(item, index) in spacesList"
          :key="index"
          class="list__item"
          :data-level="item.level"
          :data-category="item.category"
          :data-space="item.space"
      >
        <a href="#" class="list__link">{{ item.name }}</a>
      </li>
    </ul>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      spacesList: [
        { name: 'The Wizard', level: 1, category: 1, space: 1.08 },
        { name: 'Apple Heart', level: 1, category: 1, space: 1.01 },
        { name: 'Crazy Banana', level: 1, category: 1, space: 1.02 },
        { name: 'The Eggplanthead', level: 2, category: 1, space: 2.05 },
        { name: 'Smoothies & Soul', level: 1, category: 1, space: 1.09 },
        { name: 'Seed of Life', level: 1, category: 1, space: 1.06 },
        { name: 'Raw Delight', level: 1, category: 1, space: 1.07 },
        { name: 'Grilled Chipotle', level: 2, category: 1, space: 2.01 },
        { name: 'Oolong House', level: 3, category: 1, space: 3.01 },
        { name: 'Cold Soup Kitchen', level: 4, category: 1, space: 4.01 },
        { name: 'Superfood', level: 2, category: 1, space: 2.06 },
        { name: 'Love 2 Cook', level: 4, category: 2, space: 4.06 },
        { name: 'Permaculture Hub', level: 4, category: 2, space: 4.07 },
        { name: 'Folding Life', level: 1, category: 2, space: 1.03 },
        { name: 'Rocketship Tech', level: 2, category: 2, space: 2.02 },
        { name: 'Which Bug?', level: 2, category: 2, space: 2.03 },
        { name: 'Enlightened Path', level: 3, category: 2, space: 3.02 },
        { name: 'Docu Dome', level: 4, category: 2, space: 4.02 },
        { name: 'Little Artist', level: 4, category: 3, space: 4.03 },
        { name: 'Your Last Shirt', level: 3, category: 3, space: 3.04 },
        { name: 'Tool Exchange', level: 2, category: 3, space: 2.08 },
        { name: 'Dress me not', level: 1, category: 3, space: 1.04 },
        { name: 'Cognitio', level: 2, category: 3, space: 2.04 },
        { name: 'What makes us walk', level: 3, category: 3, space: 3.03 },
        { name: 'No Princess', level: 2, category: 3, space: 2.07 },
        { name: 'Star Gazer', level: 3, category: 4, space: 3.07 },
        { name: 'Space 16', level: 4, category: 4, space: 4.04 },
        { name: 'Breathe', level: 3, category: 4, space: 3.05 },
        { name: 'Meditation Garden', level: 1, category: 4, space: 1.05 },
        { name: 'Hot Tub Festival', level: 4, category: 4, space: 4.05 },
        { name: 'Feel the Grass', level: 3, category: 4, space: 3.06 }
      ]
    }
  }
}
</script>

<style scoped>
/* Add your CSS here */
</style>
