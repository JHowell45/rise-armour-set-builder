import Vue from "vue"
import VueRouter from "vue-router"

import ArmourPiece from '@/components/ArmourPiece'

Vue.use(VueRouter)

const routes = [
    {path: 'armour-piece/:name', component: ArmourPiece}
]

const router = new VueRouter({
    routes: routes,
    mode: 'history'
})
export default router