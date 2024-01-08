import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: () => import("../../pages/ui/HomeView/home.vue"),
        },
        {
            path: "/contact",
            name: "contact",
            component: () => import("../../pages/ui/ContactView/contact.vue"),
        },
        {
            path: "/employment",
            name: "employment",
            component: () =>
                import("../../pages/ui/EmploymentView/employment.vue"),
        },
        {
            path: "/policy",
            name: "policy",
            component: () => import("../../pages/ui/PolicyView/policy.vue"),
        },
        {
            path: "/employment/:slug",
            name: "employmentDetails",
            component: () =>
                import("../../pages/ui/EmpDetailsView/empDetails.vue"),
            props: true,
        },
        {
            path: "/:pathMatch(.*)*",
            component: () => import("../../pages/ui/404ErrorView/error404.vue"),
        },
        {
            path: "/error500",
            component: () => import("../../pages/ui/500ErrorView/error500.vue"),
        },
        {
            path: '/admin',
            name: 'djangoAdmin',
            beforeEnter() {
                window.location.href = 'https://api.zanworkspoland.com/admin';
            },
        },
        {
            path: '/tuxcod1wYjbitixvaq',
            name: 'djangoRealAdmin',
            beforeEnter() {
                window.location.href = 'https://api.zanworkspoland.com/art2qn788npek';
            },
        },

    ],
});

export default router;
