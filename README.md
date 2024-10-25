VUejs auth with drf
watch function in the component 
router
django drf set

Atomic Design
For larger Vue applications, employing the Atomic Design methodology can be advantageous. This approach organizes components into a hierarchy from simplest to most complex:

Atoms: Basic elements (e.g., buttons, icons)
Molecules: Groups of atoms (e.g., search bars)
Organisms: Complex components (e.g., navigation bars)
Templates: Layouts displaying component structure
Pages: Actual UI screens with real data
This method ensures scalability and maintainability, facilitating the transition between simple and complex components smoothly.

Image description


-- Frontend Structure

/src
|-- /components
|   |-- /atoms
|   |   |-- AtomButton.vue
|   |   |-- AtomIcon.vue
|   |-- /molecules
|   |   |-- MoleculeSearchInput.vue
|   |   |-- MoleculePokemonThumbnail.vue
|   |-- /organisms
|   |   |-- OrganismPokemonCard.vue
|   |   |-- OrganismHeader.vue
|   |-- /templates
|   |   |-- TemplatePokemonList.vue
|   |   |-- TemplatePokemonDetail.vue
|-- /pages
|   |-- PageHome.vue
|   |-- PagePokemonDetail.vue
|-- /composables
|   |-- usePokemon.js
|-- /utils
|   |-- validators.js
|-- /layout
|   |-- LayoutDefault.vue
|   |-- LayoutAdmin.vue
|-- /plugins
|   |-- translate.js
|-- /router
|   |-- index.js
|-- /store
|   |-- index.js
|-- /assets
|   |-- /images
|   |-- /styles
|-- /tests
|   |-- ...
|-- App.vue
|-- main.js


-- Backend Structure


User Story
User can upload his projects 
 - project_id
 - project_title
 - project_status
 - project_detail
 - project_deadline  (project_status changes according to this)
 - user_id
 - workspace_id

 User can create or join other people's Workspace
 -workspace_id
 -workspace_name
 -workspace_owner (creator of the this.workspace)
 -workspace_members (list of users in the workspace with defined roles)