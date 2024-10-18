import { useRef, useState, useEffect } from "react";

import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import { useForm } from "react-hook-form";
import { Toast } from "primereact/toast";
import { Calendar } from "primereact/calendar";
import { Nullable } from "primereact/ts-helpers";

import { Patient } from "../interfaces/patient_interface";
import { GenderOptions, CityOptions } from "../common/utils/types";
import { createPatient } from "../api/patients.api";

interface PatientCreateFormProps {
    onPatientCreated: () => void;
}

export default function CreatePatientForm({ onPatientCreated }: PatientCreateFormProps) {
    const { register, handleSubmit, formState: { errors }, setValue } = useForm<Patient>();
    const [visible, setVisible] = useState<boolean>(false);
    const [registrationDate, setRegistrationDate] = useState<Nullable<Date>>(null);
    const [birthDate, setBirthDate] = useState<Nullable<Date>>(null);
    const [isOpen, setIsOpen] = useState<boolean>(false);

    const toggleModal = () => {
        setIsOpen(!isOpen);
    };

    useEffect(() => {
        setValue('birth_date', birthDate ? birthDate.toISOString() : '');
        setValue('registration_date', registrationDate ? registrationDate.toISOString() : '');
    }, [birthDate, registrationDate, setValue]);

    const toast = useRef<Toast>(null);
    const showSuccess = () => {
        toast.current?.show(
            {
                severity:'success',
                summary:'Success',
                detail:'Patient added correctly',
                life:3000
            }
        );
    }

    const onSubmit = async (data: Patient) => {
        const transformedData = {
            ...data,
            age: Number(data.age),
        };

        try {
            await createPatient(transformedData);
            showSuccess();
            onPatientCreated();
        } catch (error) {
            console.error("Error while creatin patient: ", error);
        }
    }

    return (
        <div className="card flex justify-content-end">
            <Button label="New Patient" icon="pi pi-external-link" onClick={() => setVisible(true)} />
            <Dialog header="Add a new patient" visible={visible} onHide={() => {if (!visible) return; setVisible(false); }}
                style={{ width: '50vw' }} breakpoints={{ '960px': '75vw', '641px': '100vw' }}>

                <form onSubmit={handleSubmit(onSubmit)}>
                    <label className="block text-gray-700">Full name</label>
                    <input {...register('name', {
                        required: true,
                        pattern: /^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$/i
                        })}
                        className="border p-2 w-full mb-2 rounded" 
                        placeholder="John Doe"
                    />
                    {errors?.name?.type === 'required' && <p className="text-red-500">This field is required</p>}
                    {errors?.name?.type === 'pattern' && <p className="text-red-500">Alphabetical characters only</p>}

                    <label className="block text-gray-700">Age</label>
                    <input type="number" {...register('age', {
                        required: true,
                        max: 18,
                        pattern: /^[0-9]+$/
                        })}
                        className="border p-2 w-full mb-2 rounded"
                    />
                    {errors?.age?.type === 'required' && <p className="text-red-500">This field is required</p>}
                    {errors?.age?.type === 'pattern' && <p className="text-red-500">Age must be number</p>}
                    {errors?.age?.type === 'max' && <p className="text-red-500">Pacient must be a minor</p>}

                    <label className="block text-gray-700">Gender</label>
                    <select {...register('gender', {required: true})}
                        className="border p-2 w-full mb-2 rounded">
                        <option value="">Select gender</option>
                        {GenderOptions.map((gender) => (
                            <option key={gender.id} value={gender.id}>
                                {gender.label}
                            </option>
                        ))}
                    </select>
                    {errors?.gender && <p className="text-red-500">This field is required</p>}

                    <label className="block text-gray-700">Birthdate</label>
                    <Calendar {...register('birth_date', {required: true})}
                        id="buttondisplay" value={birthDate} onChange={(e) => setBirthDate(e.value)} showIcon 
                        className="border p-2 w-full mb-2 rounded"
                    />
                    {errors?.birth_date && <p className="text-red-500">This field is required</p>}


                    <label className="block text-gray-700">City of origin</label>
                    <select {...register('city_origin', {required: true})}
                        className="border p-2 w-full mb-2 rounded">
                        <option value="">Select your city</option>
                        {CityOptions.map((city) => (
                            <option key={city.value} value={city.value}>
                                {city.name}
                            </option>
                        ))}
                    </select>
                    {errors?.city_origin && <p className="text-red-500">This field is required</p>}


                    <label className="block text-gray-700">Hopital of origin</label>
                    <input {...register('hospital_origin', {
                        required: true,
                        pattern: /^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$/i
                        })}
                        className="border p-2 w-full mb-2 rounded" 
                    />
                    {errors?.hospital_origin?.type === 'required' && <p className="text-red-500">Alphabetical characters only</p>}
                    {errors?.hospital_origin?.type === 'pattern' && <p className="text-red-500">This field is required</p>}

                    <label className="block text-gray-700">Registration date</label>
                    <Calendar {...register('registration_date', {required: true})}
                        id="buttondisplay" value={registrationDate} onChange={(e) => setRegistrationDate(e.value)} showIcon 
                        className="border p-2 w-full mb-2 rounded"
                    />
                    {errors?.registration_date && <p className="text-red-500">This field is required</p>}

                    <label className="block text-gray-700">Tutor name</label>
                    <input {...register('tutor_name', {
                        required: true,
                        pattern: /^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$/i
                        })}
                        className="border p-2 w-full mb-2 rounded" 
                        placeholder="Michael Doe"
                    />
                    {errors?.tutor_name?.type === 'required' && <p className="text-red-500">This field is required</p>}
                    {errors?.tutor_name?.type === 'pattern' && <p className="text-red-500">Alphabetical characters only</p>}

                    <label className="block text-gray-700">Tutor phone</label>
                    <input type="tel" {...register('tutor_phone',
                        {
                            required: true,
                            pattern: /^[0-9]{10}$/,
                        }
                        )}
                        placeholder="1234567890"
                        className="border p-2 w-full mb-2 rounded"
                    />
                    {errors?.tutor_phone?.type === 'required' && <p className="text-red-500">This field is required</p>}
                    {errors?.tutor_phone?.type === 'pattern' && <p className="text-red-500">Phone should have 10 digits</p>}

                    <input type="submit" className="bg-blue-500 text-white px-4 py-2 mt-4 rounded hover:bg-blue-700 cursor-pointer w-full" value="Create Patient" onSubmit={toggleModal} />
                </form>
            </Dialog>
        </div>
    )
}
        