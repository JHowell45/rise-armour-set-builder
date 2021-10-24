<template>
    <router-link :to="`/armour-piece/${armourPiece.name}`">{{ displayName }}</router-link>
</template>

<script>
export default ({
    name: 'ArmourPiece',
    props: {
        armourPiece: {
            type: Object,
            required: true
        }
    },
    computed: {
        displayName() {
            return (
                this.armourPiece.name
            )
        }
    }
})
</script>
