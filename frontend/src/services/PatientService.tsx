export const PatientService = {
    getData() {
        return [
            {
                id: 1,
                name: 'Ruben Alvarado',
                age: 10,
                gender: 'male',
                birth_date: '2015-09-13',
                city_origin: 'Oxkutzcab',
                registration_date: '2016-09-13',
                hospital_origin: 'Ohoran',
                tutor_name: 'Arturo Alvarado',
                tutor_phone: '9971214242',
            },
            {
                id: 2,
                name: 'Monica Garcilazo',
                age: 5,
                gender: 'female',
                birth_date: '2015-05-31',
                city_origin: 'Merida',
                registration_date: '2016-09-13',
                hospital_origin: 'Pensiones',
                tutor_name: 'Marcy Cuevas',
                tutor_phone: '9996459013',
            },
            {
                id: 3,
                name: 'Ian Aguilar',
                age: 7,
                gender: 'male',
                birth_date: '2015-08-17',
                city_origin: 'Chetumal',
                registration_date: '2016-09-13',
                hospital_origin: 'Clinica de Merida',
                tutor_name: 'Claudia Ramirez',
                tutor_phone: '9975564241',
            },
            {
                id: 4,
                name: 'Pablo Gamboa',
                age: 8,
                gender: 'male',
                birth_date: '2015-10-13',
                city_origin: 'Monterrey',
                registration_date: '2016-09-13',
                hospital_origin: 'CMA',
                tutor_name: 'Pablo Gamboa',
                tutor_phone: '9971216572',
            },
            {
                id: 5,
                name: 'Abraham Espinosa',
                age: 10,
                gender: 'male',
                birth_date: '2015-09-15',
                city_origin: 'Campeche',
                registration_date: '2016-09-13',
                hospital_origin: 'Pensiones',
                tutor_name: 'Abraham Espinosa',
                tutor_phone: '9981214242',
            },
        ];
    },

    getPatientsSmall() {
        return Promise.resolve(this.getData().slice(0, 10));
    },

    getPatientsMedium() {
        return Promise.resolve(this.getData().slice(0, 50));
    },

    getPatientsLarge() {
        return Promise.resolve(this.getData().slice(0, 200));
    },

    getPatientsXLarge() {
        return Promise.resolve(this.getData());
    },

    getPatients(params: { [key: string]: string }) {
        const queryParams = params
            ? Object.keys(params)
                  .map((k) => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
                  .join('&')
            : '';

        return fetch('https://www.primefaces.org/data/customers?' + queryParams).then((res) => res.json());
    }

};