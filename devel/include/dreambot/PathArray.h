// Generated by gencpp from file dreambot/PathArray.msg
// DO NOT EDIT!


#ifndef DREAMBOT_MESSAGE_PATHARRAY_H
#define DREAMBOT_MESSAGE_PATHARRAY_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dreambot
{
template <class ContainerAllocator>
struct PathArray_
{
  typedef PathArray_<ContainerAllocator> Type;

  PathArray_()
    : x()
    , y()  {
    }
  PathArray_(const ContainerAllocator& _alloc)
    : x(_alloc)
    , y(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _x_type;
  _x_type x;

   typedef std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> _y_type;
  _y_type y;





  typedef boost::shared_ptr< ::dreambot::PathArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dreambot::PathArray_<ContainerAllocator> const> ConstPtr;

}; // struct PathArray_

typedef ::dreambot::PathArray_<std::allocator<void> > PathArray;

typedef boost::shared_ptr< ::dreambot::PathArray > PathArrayPtr;
typedef boost::shared_ptr< ::dreambot::PathArray const> PathArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dreambot::PathArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dreambot::PathArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dreambot::PathArray_<ContainerAllocator1> & lhs, const ::dreambot::PathArray_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dreambot::PathArray_<ContainerAllocator1> & lhs, const ::dreambot::PathArray_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dreambot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dreambot::PathArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dreambot::PathArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::PathArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::PathArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::PathArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::PathArray_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dreambot::PathArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "796182af49bd48aa8ba60ed21519725c";
  }

  static const char* value(const ::dreambot::PathArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x796182af49bd48aaULL;
  static const uint64_t static_value2 = 0x8ba60ed21519725cULL;
};

template<class ContainerAllocator>
struct DataType< ::dreambot::PathArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dreambot/PathArray";
  }

  static const char* value(const ::dreambot::PathArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dreambot::PathArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64[] x\n"
"float64[] y\n"
;
  }

  static const char* value(const ::dreambot::PathArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dreambot::PathArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PathArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dreambot::PathArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dreambot::PathArray_<ContainerAllocator>& v)
  {
    s << indent << "x[]" << std::endl;
    for (size_t i = 0; i < v.x.size(); ++i)
    {
      s << indent << "  x[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.x[i]);
    }
    s << indent << "y[]" << std::endl;
    for (size_t i = 0; i < v.y.size(); ++i)
    {
      s << indent << "  y[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.y[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // DREAMBOT_MESSAGE_PATHARRAY_H
