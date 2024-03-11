'use client';
import React, { useEffect } from 'react'
import { redirect } from 'next/navigation'

type Props = {}

const Page = (props: Props) => {

  useEffect(() => {
    redirect('/')
  }
  , [])

  return (
    <></>
  )
}

export default Page